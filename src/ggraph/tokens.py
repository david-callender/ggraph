from typing import Literal

type Num = int | float


class LexemeType:
    NumLit: Literal[0] = 0
    Name: Literal[1] = 1
    Plus: Literal[2] = 2
    Minus: Literal[3] = 3
    Star: Literal[4] = 4
    Slash: Literal[5] = 5
    Caret: Literal[6] = 6
    OpenParen: Literal[7] = 7
    CloseParen: Literal[8] = 8
    Comma: Literal[9] = 9
    Eq: Literal[10] = 10


class LexemeNumLit:
    tag = LexemeType.NumLit
    value: Num

    def __init__(self, value):
        self.tag = LexemeType.NumLit
        self.value = value


class LexemeName:
    tag = LexemeType.Name
    value: str

    def __init__(self, value):
        self.tag = LexemeType.Name
        self.value = value


class LexemePlus:
    tag = LexemeType.Plus

    def __init__(self):
        self.tag = LexemeType.Plus


class LexemeMinus:
    tag = LexemeType.Minus

    def __init__(self):
        self.tag = LexemeType.Minus


class LexemeStar:
    tag = LexemeType.Star

    def __init__(self):
        self.tag = LexemeType.Star


class LexemeSlash:
    tag = LexemeType.Slash

    def __init__(self):
        self.tag = LexemeType.Slash


class LexemeCaret:
    tag = LexemeType.Caret

    def __init__(self):
        self.tag = LexemeType.Caret


class LexemeOpenParen:
    tag = LexemeType.OpenParen

    def __init__(self):
        self.tag = LexemeType.OpenParen


class LexemeCloseParen:
    tag = LexemeType.CloseParen

    def __init__(self):
        self.tag = LexemeType.CloseParen


class LexemeComma:
    tag = LexemeType.Comma

    def __init__(self):
        self.tag = LexemeType.Comma


class LexemeEq:
    tag = LexemeType.Eq

    def __init__(self):
        self.tag = LexemeType.Eq


type Lexeme = (
    LexemeNumLit
    | LexemeName
    | LexemePlus
    | LexemeMinus
    | LexemeStar
    | LexemeSlash
    | LexemeCaret
    | LexemeOpenParen
    | LexemeCloseParen
    | LexemeComma
    | LexemeEq
)


class TokenType:
    NumLit: Literal[1] = 1
    Var: Literal[2] = 2
    Add: Literal[3] = 3
    Sub: Literal[4] = 4
    Mul: Literal[5] = 5
    Div: Literal[6] = 6
    Pow: Literal[7] = 7
    FuncCall: Literal[8] = 8
    FuncDef: Literal[9] = 9


class TokenNumLit:
    tag = TokenType.NumLit
    value: Num

    def __init__(self, value: Num):
        self.tag = TokenType.NumLit
        self.value = value


class TokenVar:
    tag = TokenType.Var
    name: str

    def __init__(self):
        self.tag = TokenType.Var


class TokenAdd:
    tag = TokenType.Add

    def __init__(self):
        self.tag = TokenType.Add


class TokenSub:
    tag = TokenType.Sub

    def __init__(self):
        self.tag = TokenType.Sub


class TokenMul:
    tag = TokenType.Mul

    def __init__(self):
        self.tag = TokenType.Mul


class TokenDiv:
    tag = TokenType.Div

    def __init__(self):
        self.tag = TokenType.Div


class TokenPow:
    tag = TokenType.Pow

    def __init__(self):
        self.tag = TokenType.Pow


class TokenFuncCall:
    tag = TokenType.FuncCall
    name: str
    num_args: int

    def __init__(self, name: str, num_args: int):
        self.tag = TokenType.FuncCall
        self.name = name
        self.num_args = num_args


class TokenFuncDef:
    tag = TokenType.FuncDef
    name: str
    args: list[str]
    body: list[Token]

    def __init__(self):
        self.tag = TokenType.FuncDef


type Token = (
    TokenNumLit
    | TokenVar
    | TokenAdd
    | TokenSub
    | TokenMul
    | TokenDiv
    | TokenPow
    | TokenFuncCall
    | TokenFuncDef
)
