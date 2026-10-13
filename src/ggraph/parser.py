from ggraph.lexer import *
from ggraph.tokens import *
from collections.abc import Iterable, Iterator
from more_itertools import peekable


def lexeme_to_token(lexeme: Lexeme) -> Token:
    """Parses one simple lexeme (such as an operator or literal) into a token"""
    match lexeme.tag:
        case LexemeType.NumLit:
            return TokenNumLit(lexeme.value)
        case LexemeType.Plus:
            return TokenAdd()
        case LexemeType.Minus:
            return TokenSub()
        case LexemeType.Star:
            return TokenMul()
        case LexemeType.Slash:
            return TokenDiv()
        case LexemeType.Caret:
            return TokenPow()
    raise ParserError(f"Non-simple token provided to lexeme_to_token: {lexeme}")


class ParserError(Exception):
    pass


class Parser:
    lexeme_stream: peekable[Lexeme]
    stack: list[Lexeme]
    output: list[Token]
    last_func_args: int

    def __init__(self, lexeme_stream: Iterable[Lexeme]) -> None:
        self.lexeme_stream = peekable(lexeme_stream)
        self.stack = []
        self.output = []
        self.last_func_args = 1

    def __iter__(self) -> Iterator[Token]:
        stream = self.parse()
        return iter(stream)

    def parse(self) -> list[Token]:
        for lexeme in self.lexeme_stream:
            match lexeme.tag:
                case LexemeType.NumLit:
                    self.output.append(lexeme_to_token(lexeme))
                case LexemeType.Name:
                    self.parse_name(lexeme)
                    continue
                case LexemeType.Comma:
                    self.parse_comma()
                case LexemeType.OpenParen:
                    self.stack.append(lexeme)
                case LexemeType.CloseParen:
                    self.parse_close_paren()
                # All of the special operators have now been dealt with,
                # and we can parse the regular operators.
                case _:
                    # Here it is safe to assume, as we have already checked for any other
                    # lexeme types, that lexeme is a LexemeOp. Thus, we change its type.
                    op: LexemeOp = lexeme
                    self.parse_op(op)

        for lexeme in self.stack[::-1]:
            # Only simple operators should be left by now.
            self.output.append(lexeme_to_token(lexeme))

        return self.output

    def parse_name(self, lexeme: LexemeName) -> None:
        if lexeme.value[0].isupper():
            if (
                # We raise a ParserError if there is a function call not followed by parens
                # (it's at the end of the stream, or followed by anything other than a openparen)
                self.lexeme_stream.peek(None) == None
                or self.lexeme_stream.peek().tag != LexemeType.OpenParen
            ):
                raise ParserError("Function call is missing parentheses")
            # Only function call lexemes end up on the operator stack
            self.stack.append(lexeme)
        else:
            # ... vars go straight to the output
            self.output.append(TokenVar(lexeme.value))

    def parse_comma(self) -> None:
        try:
            self.slurp_paren()
            self.last_func_args += 1
        except IndexError:
            raise ParserError("Comma placed outside of parentheses")

    def parse_close_paren(self) -> None:
        try:
            self.slurp_paren()
            if self.stack.pop().tag != LexemeType.OpenParen:
                raise ParserError(
                    "Unreachable: Non-left-parentheses left found after parsing right parentheses"
                )
            # Since only names representing a function call end up on the stack, that the
            # top of the stack is a name is enough information alone to guess a function
            if self.stack and self.stack[-1].tag == LexemeType.Name:
                # ty really doesn't like this but I don't know a way to signal that this
                # only happens if self.stack.pop().value is guaranteed to be a LexemeName
                stack_top: LexemeName = self.stack.pop()
                self.output.append(TokenFuncCall(stack_top.value, self.last_func_args))
                self.last_func_args = 1
            elif self.last_func_args != 1:
                raise ParserError("Comma inside non-function call")
        except IndexError:
            raise ParserError("Mismatched parentheses")

    def parse_op(self, lexeme: LexemeOp) -> None:
        while self.stack_has_precedence(lexeme):
            self.output.append(lexeme_to_token(self.stack.pop()))

        self.stack.append(lexeme)

    def slurp_paren(self) -> None:
        while self.stack[-1].tag != LexemeType.OpenParen:
            self.output.append(lexeme_to_token(self.stack.pop()))

    def stack_has_precedence(self, op: LexemeOp) -> bool:
        # If there's nothing on the stack, it doesn't have precedence
        if not self.stack:
            return False

        stack_top = self.stack[-1]

        if stack_top.tag == LexemeType.OpenParen:
            return False

        # Now it is safe to assume that the lexeme is an operator, as other prior functions
        # will have made sure that a name will not be found above its corresponding
        # left paren on the stack, so we change its type here via a self-assignment
        stack_top_op: LexemeOp = stack_top

        if stack_top_op.precedence > op.precedence:
            return True

        return (
            stack_top_op.precedence == op.precedence
            and stack_top_op.associativity == LexemeAssociativity.Left
        )
