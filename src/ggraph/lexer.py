from ggraph import tokens


class LexerError(Exception):
    message: str

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class Lexer:
    expression: str
    idx: int  # Strings are iterable but do not have a peeking implementation needed for some lexing functions
    cache: tokens.Lexeme | None

    def __init__(self, expression: str):
        self.expression = expression.replace(" ", "")
        self.idx = 0
        self.cache = self.next_tok()

    def __iter__(self) -> Lexer:
        return self

    def __next__(self) -> tokens.Lexeme:
        ret: tokens.Lexeme
        if self.cache == None:
            raise StopIteration
        else:
            ret = self.cache

        if self.idx >= len(self.expression):
            self.cache = None
        else:
            self.cache = self.next_tok()

        return ret

    def peek(self) -> tokens.Lexeme | None:
        return self.cache

    def next_tok(self) -> tokens.Lexeme:
        next_char = self.expression[self.idx]

        if self.expression[self.idx].isnumeric():
            return self.lex_num_literal()
        elif self.expression[self.idx].isalpha():
            return self.lex_name()

        match next_char:
            case "+":
                self.idx += 1
                return tokens.LexemePlus()
            case "-":
                self.idx += 1
                return tokens.LexemeMinus()
            case "*":
                self.idx += 1
                return tokens.LexemeStar()
            case "/":
                self.idx += 1
                return tokens.LexemeSlash()
            case "^":
                self.idx += 1
                return tokens.LexemeCaret()
            case "(":
                self.idx += 1
                return tokens.LexemeOpenParen()
            case ")":
                self.idx += 1
                return tokens.LexemeCloseParen()
            case ",":
                self.idx += 1
                return tokens.LexemeComma()
            case "=":
                self.idx += 1
                return tokens.LexemeEq()

        raise LexerError(f"Invalid character in math expression: {next_char}")

    def lex_num_literal(self) -> tokens.LexemeNumLit:
        next_char = self.expression[self.idx]
        num_str: str = ""
        num: tokens.Num = 0
        is_float: bool = False

        while next_char.isnumeric() or next_char == ".":
            if next_char == "." and (not is_float):
                is_float = True
            elif next_char == "." and is_float:
                raise LexerError("Numbers may have at most one decimal point")
            num_str += next_char
            self.idx += 1
            if self.idx < len(self.expression):
                next_char = self.expression[self.idx]
            else:
                break  # End the loop when we've hit the end of the expression

        if is_float:
            num = float(num_str)
        else:
            num = int(num_str)

        return tokens.LexemeNumLit(num)

    def lex_name(self) -> tokens.LexemeName:
        next_char = self.expression[self.idx]
        name: str = ""

        while next_char.isalpha():
            name += next_char
            self.idx += 1
            if self.idx < len(self.expression):
                next_char = self.expression[self.idx]
            else:
                break  # End the loop when we've hit the end of the expression

        return tokens.LexemeName(name)
