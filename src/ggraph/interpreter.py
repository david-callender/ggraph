from typing import assert_never

from ggraph.builtins import construct_builtin_map, safePow
from ggraph.errors import InterpreterError
from ggraph.tokens import Token, TokenFuncEnd, TokenType


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
    builtins = construct_builtin_map()

    stack = []

    def pop_float() -> float:
        if len(stack) == 0:
            raise InterpreterError(
                "misaligned stack, tried to pop a float from an empty stack"
            )
        return stack.pop()

    def pop_int() -> int:
        if len(stack) == 0:
            raise InterpreterError(
                "misaligned stack, tried to pop an int from an empty stack"
            )
        value = stack.pop()
        int_value = int(value)
        if value != float(int_value):
            print(f"Expected int to function {builtin.name}")

        return int_value

    env = start_env

    while len(program) != 0:
        token = program.pop()
        match token.tag:
            case TokenType.NumLit:
                stack.append(token.value)

            case TokenType.Var:
                value = env.search_var(token.name)
                if value is None:
                    raise InterpreterError(f"Couldn't find variable {token.name}")
                stack.append(value)

            case TokenType.Add:
                a = pop_float()
                b = pop_float()
                stack.append(b + a)

            case TokenType.Sub:
                a = pop_float()
                b = pop_float()
                stack.append(b - a)

            case TokenType.Mul:
                a = pop_float()
                b = pop_float()
                stack.append(b * a)

            case TokenType.Div:
                a = pop_float()
                b = pop_float()
                stack.append(b / a)

            case TokenType.Pow:
                a = pop_float()
                b = pop_float()
                stack.append(safePow(b, a))

            case TokenType.FuncCall:
                if token.name in builtins:
                    builtin = builtins[token.name]

                    match builtin.typed_impl:
                        case ("float", impl):
                            stack.append(impl(pop_float()))
                        case ("float,float", impl):
                            a = pop_float()
                            b = pop_float()
                            stack.append(impl(b, a))
                        case ("float,int", impl):
                            a = pop_int()
                            b = pop_float()
                            stack.append(impl(b, a))
                        case ("int,int", impl):
                            a = pop_int()
                            b = pop_int()
                            stack.append(impl(b, a))
                        case _:
                            assert_never(builtin.typed_impl)

                else:
                    func_object = env.search_funcs(token.name)
                    if func_object is None:
                        raise InterpreterError(f"Failed to find function {token.name}")

                    new_env = Env(env)
                    for arg_type in func_object.args:
                        value = stack.pop()
                        new_env.vars[arg_type] = value

                    program.append(TokenFuncEnd())
                    program.extend(func_object.body)
                    env = new_env

            case TokenType.FuncEnd:
                if env.parent is None:
                    raise InterpreterError("misaligned env stack")
                env = env.parent

            case TokenType.FuncDef:
                func_object = RuntimeFunc(token.name, token.args, token.body)
                env.funcs[token.name] = func_object

            case TokenType.Negate:
                a = pop_float()
                stack.append(-a)

            case _:
                assert_never(token.tag)

    result = stack[0]
    return result
