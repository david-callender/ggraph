from collections import deque
from typing import Iterable

from ggraph.lexer import *
from ggraph.tokens import *


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
    message: str

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class Parser:
    token_stream: Iterable[Lexeme]
    stack: list[Lexeme]
    output: list[Token]

    def __init__(self, ls: Iterable[Lexeme]):
        self.lexeme_stream = ls
        self.stack = []
        self.output = []

    def parse(self):
        for lexeme in self.lexeme_stream:
            match lexeme.tag:
                case LexemeType.NumLit:
                    self.output.append(lexeme_to_token(lexeme))
                case LexemeType.Name:
                    if lexeme.value[0].isupper():
                        # Only function call lexemes end up on the operator stack
                        self.stack.append(lexeme)
                    else:
                        # ... vars go straight to the output
                        self.output.append(TokenVar(lexeme.value))
                    continue
                case LexemeType.Comma:
                    self.parse_comma()
                case LexemeType.OpenParen:
                    self.stack.append(lexeme)
                case LexemeType.CloseParen:
                    self.parse_close_paren()

    def parse_close_paren(self):
        try:
            while self.stack[-1].tag != LexemeType.OpenParen:
                self.output.append(lexeme_to_token(self.stack.pop()))
            if self.stack.pop().tag != LexemeType.OpenParen:
                raise ParserError(
                    "Unreachable: Non-left-parentheses left found after parsing right parentheses"
                )
            if self.stack[-1].tag == LexemeType.Name:
                # ty thinks this is unreachable but I'm pretty sure it's not since the openparen gets popped
                self.output.append(self.stack.pop().value, 0)
        except IndexError:
            raise ParserError("Mismatched parentheses")

    def parse_comma(self):
        while self.stack[-1].tag != LexemeType.OpenParen:
            self.output.append(lexeme_to_token(self.stack.pop()))
