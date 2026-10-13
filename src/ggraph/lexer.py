from more_itertools import peekable

from ggraph.tokens import (
    Lexeme,
    LexemeNumLit,
    LexemeName,
    LexemePlus,
    LexemeMinus,
    LexemeStar,
    LexemeSlash,
    LexemeCaret,
    LexemeOpenParen,
    LexemeCloseParen,
    LexemeComma,
    LexemeEq,
)


class LexerError(Exception):
    pass


class Lexer:
    expression: peekable

    def __init__(self, expression: str):
        self.expression = peekable(expression.replace(" ", ""))

    def __iter__(self) -> Lexer:
        return self

    def __next__(self) -> Lexeme:
        return self.next_tok()

    def next_tok(self) -> Lexeme:
        next_char = self.expression.peek()

        if next_char.isnumeric():
            return self.lex_num_literal()
        elif next_char.isalpha():
            return self.lex_name()

        match next_char:
            case "+":
                next(self.expression)
                return LexemePlus()
            case "-":
                next(self.expression)
                return LexemeMinus()
            case "*":
                next(self.expression)
                return LexemeStar()
            case "/":
                next(self.expression)
                return LexemeSlash()
            case "^":
                next(self.expression)
                return LexemeCaret()
            case "(":
                next(self.expression)
                return LexemeOpenParen()
            case ")":
                next(self.expression)
                return LexemeCloseParen()
            case ",":
                next(self.expression)
                return LexemeComma()
            case "=":
                next(self.expression)
                return LexemeEq()

        raise LexerError(f"Invalid character in math expression: {next_char}")

    def lex_num_literal(self) -> LexemeNumLit:
        next_char: str = self.expression.peek()
        num_str: str = ""
        num: float
        is_float: bool = False

        while next_char and (next_char.isnumeric() or next_char == "."):
            next(self.expression)
            if next_char == "." and (not is_float):
                is_float = True
            elif next_char == "." and is_float:
                raise LexerError("Numbers may have at most one decimal point")
            num_str += next_char
            next_char: str | None = self.expression.peek(None)

        if is_float:
            num = float(num_str)
        else:
            num = int(num_str)

        return LexemeNumLit(num)

    def lex_name(self) -> LexemeName:
        next_char: str | None = self.expression.peek()
        name: str = ""

        while next_char and next_char.isalpha():
            next(self.expression)
            name += next_char
            next_char: str | None = self.expression.peek(None)

        return LexemeName(name)
