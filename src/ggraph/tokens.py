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
    UnaryMinus: Literal[11] = 11


class LexemeNumLit:
    tag = LexemeType.NumLit
    value: float

    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class LexemeName:
    tag = LexemeType.Name
    value: str

    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class LexemePlus:
    tag = LexemeType.Plus
    precedence = 10
    associativity = LexemeAssociativity.Left

    def __str__(self) -> str:
        return "+"


class LexemeMinus:
    tag = LexemeType.Minus
    precedence = 10
    associativity = LexemeAssociativity.Left

    def __str__(self) -> str:
        return "-"


class LexemeStar:
    tag = LexemeType.Star
    precedence = 20
    associativity = LexemeAssociativity.Left

    def __str__(self) -> str:
        return "*"


class LexemeSlash:
    tag = LexemeType.Slash
    precedence = 20
    associativity = LexemeAssociativity.Left

    def __str__(self) -> str:
        return "/"


class LexemeCaret:
    tag = LexemeType.Caret
    precedence = 30
    associativity = LexemeAssociativity.Right

    def __str__(self) -> str:
        return "^"


class LexemeOpenParen:
    tag = LexemeType.OpenParen

    def __str__(self) -> str:
        return "("


class LexemeCloseParen:
    tag = LexemeType.CloseParen

    def __str__(self) -> str:
        return ")"


class LexemeComma:
    tag = LexemeType.Comma

    def __str__(self) -> str:
        return ","


class LexemeEq:
    tag = LexemeType.Eq

    def __str__(self) -> str:
        return "="


class LexemeUnaryMinus:
    tag = LexemeType.UnaryMinus
    precedence = 40
    associativity = LexemeAssociativity.Right


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
    | LexemeUnaryMinus
)

type LexemeOp = LexemePlus | LexemeMinus | LexemeStar | LexemeSlash | LexemeCaret


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
    Negate: Literal[10] = 10


class TokenNumLit:
    tag = TokenType.NumLit
    value: float

    def __init__(self, value: float):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class TokenVar:
    tag = TokenType.Var
    name: str

    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return str(self.name)


class TokenAdd:
    tag = TokenType.Add

    def __str__(self) -> str:
        return "+"


class TokenSub:
    tag = TokenType.Sub

    def __str__(self) -> str:
        return "-"


class TokenMul:
    tag = TokenType.Mul

    def __str__(self) -> str:
        return "*"


class TokenDiv:
    tag = TokenType.Div

    def __str__(self) -> str:
        return "/"


class TokenPow:
    tag = TokenType.Pow

    def __str__(self) -> str:
        return "^"


class TokenFuncCall:
    tag = TokenType.FuncCall
    name: str
    num_args: int

    def __init__(self, name: str, num_args: int):
        self.name = name
        self.num_args = num_args

    def __str__(self) -> str:
        return f"FuncCall({self.name} {self.num_args})"


class TokenFuncEnd:
    tag = TokenType.FuncEnd

    def __str__(self) -> str:
        return "FuncEnd"


class TokenFuncDef:
    tag = TokenType.FuncDef
    name: str
    args: list[str]
    body: list[Token]

    def __init__(self, name: str, args: list[str], body: list[Token]):
        self.name = name
        self.args = args
        self.body = body

    def __str__(self) -> str:
        return f"FuncCall({self.name} {self.args} {self.body})"


class TokenNegate:
    tag = TokenType.Negate

    def __str__(self):
        return "⁻"


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
    | TokenNegate
)
