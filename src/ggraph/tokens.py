from typing import Literal


class LexemeAssociativity:
    Left: Literal[0] = 0
    Right: Literal[1] = 1


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
    value: float

    def __init__(self, value):
        self.value = value


class LexemeName:
    tag = LexemeType.Name
    value: str

    def __init__(self, value):
        self.value = value


class LexemePlus:
    tag = LexemeType.Plus
    precedence = 10
    associativity = LexemeAssociativity.Left


class LexemeMinus:
    tag = LexemeType.Minus
    precedence = 10
    associativity = LexemeAssociativity.Left


class LexemeStar:
    tag = LexemeType.Star
    precedence = 20
    associativity = LexemeAssociativity.Left


class LexemeSlash:
    tag = LexemeType.Slash
    precedence = 20
    associativity = LexemeAssociativity.Left


class LexemeCaret:
    tag = LexemeType.Caret
    precedence = 30
    associativity = LexemeAssociativity.Right


class LexemeOpenParen:
    tag = LexemeType.OpenParen


class LexemeCloseParen:
    tag = LexemeType.CloseParen


class LexemeComma:
    tag = LexemeType.Comma


class LexemeEq:
    tag = LexemeType.Eq


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
    NumLit: Literal[0] = 0
    Var: Literal[1] = 1
    Add: Literal[2] = 2
    Sub: Literal[3] = 3
    Mul: Literal[4] = 4
    Div: Literal[5] = 5
    Pow: Literal[6] = 6
    FuncCall: Literal[7] = 7
    FuncEnd: Literal[8] = 8
    FuncDef: Literal[9] = 9


class TokenNumLit:
    tag = TokenType.NumLit
    value: float

    def __init__(self, value: float):
        self.value = value


class TokenVar:
    tag = TokenType.Var
    name: str

    def __init__(self, name: str):
        self.name = name


class TokenAdd:
    tag = TokenType.Add


class TokenSub:
    tag = TokenType.Sub


class TokenMul:
    tag = TokenType.Mul


class TokenDiv:
    tag = TokenType.Div


class TokenPow:
    tag = TokenType.Pow


class TokenFuncCall:
    tag = TokenType.FuncCall
    name: str
    num_args: int

    def __init__(self, name: str, num_args: int):
        self.name = name
        self.num_args = num_args


class TokenFuncEnd:
    tag = TokenType.FuncEnd


class TokenFuncDef:
    tag = TokenType.FuncDef
    name: str
    args: list[str]
    body: list[Token]

    def __init__(self, name: str, args: list[str], body: list[Token]):
        self.name = name
        self.args = args
        self.body = body


type Token = (
    TokenNumLit
    | TokenVar
    | TokenAdd
    | TokenSub
    | TokenMul
    | TokenDiv
    | TokenPow
    | TokenFuncCall
    | TokenFuncEnd
    | TokenFuncDef
)
