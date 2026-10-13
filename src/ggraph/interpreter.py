from typing import assert_never

from ggraph.tokens import Token, TokenFuncEnd, TokenType


class GGraphException(Exception):
    pass


class RuntimeFunc:
    name: str
    args: list[str]
    body: list[Token]

    def __init__(self, name: str, args: list[str], body: list[Token]):
        self.name = name
        self.args = args
        self.body = body


class Env:
    parent: Env | None
    vars: dict[str, float]
    funcs: dict[str, RuntimeFunc]

    def __init__(self, parent: Env | None):
        self.parent = parent
        self.vars = {}
        self.funcs = {}

    def search_var(self, name: str) -> float | None:
        env = self
        while env is not None:
            if name in env.vars:
                return env.vars[name]
            env = env.parent

    def search_funcs(self, name: str) -> RuntimeFunc | None:
        env = self
        while env is not None:
            if name in env.funcs:
                return env.funcs[name]
            env = env.parent


def interpret(program: list[Token], start_env: Env) -> float:
    stack = []

    env = start_env

    while len(program) != 0:
        token = program.pop()
        match token.tag:
            case TokenType.NumLit:
                stack.append(token.value)

            case TokenType.Var:
                value = env.search_var(token.name)
                stack.append(value)

            case TokenType.Add:
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)

            case TokenType.Sub:
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)

            case TokenType.Mul:
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)

            case TokenType.Div:
                a = stack.pop()
                b = stack.pop()
                stack.append(b / a)

            case TokenType.Pow:
                a = stack.pop()
                b = stack.pop()
                stack.append(b**a)

            case TokenType.FuncCall:
                func_object = env.search_funcs(token.name)
                if func_object is None:
                    raise GGraphException(f"Failed to find function {token.name}")

                new_env = Env(env)
                for arg in func_object.args:
                    value = stack.pop()
                    new_env.vars[arg] = value

                program.append(TokenFuncEnd())
                program.extend(func_object.body)
                env = new_env

            case TokenType.FuncEnd:
                if env.parent is None:
                    raise GGraphException("missaligned env stack")
                env = env.parent

            case TokenType.FuncDef:
                func_object = RuntimeFunc(token.name, token.args, token.body)
                env.funcs[token.name] = func_object

            case _:
                assert_never(token.tag)

    result = stack[0]
    return result
