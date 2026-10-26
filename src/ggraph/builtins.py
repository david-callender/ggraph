import math
from collections.abc import Callable
from dataclasses import dataclass
from typing import Literal

from ggraph.interpreter import InterpreterError

type ArgType = Literal["float", "int"]

x = lambda a: a + 10


@dataclass
class Builtin:
    name: str
    args: list[ArgType]
    impl: Callable[[float], float] | Callable[[float, float], float]


def safePow(base: float, power: float) -> float:
    ans = base**power
    if isinstance(ans, (int, float)):
        return ans
    raise InterpreterError("Invalid arguments to pow")


def gg_sqrt(n: float) -> float:
    return math.sqrt(n)


def gg_root(base: float, power: float) -> float:
    return safePow(base, power)


def gg_min(a: float, b: float) -> float:
    return min(a, b)


def gg_max(a: float, b: float) -> float:
    return max(a, b)


def gg_abs(n: float) -> float:
    return abs(n)


# def gg_round(n: float, precision: int) -> float:
#     return round(float, precision)


# def gg_int(n: float) -> int:
#     return


# def gg_truncate(n: float) -> float:
#     return


# def gg_lcm(a: int, b: int) -> int:
#     return


# def gg_gcd(a: int, b: int) -> int:
#     return


# def gg_nPr(n: int, r: int) -> int:
#     return


# def gg_nCr(n: int, r: int) -> int:
#     return


# def gg_exp(n: float) -> float:
#     return


# def gg_log(n: float) -> float:
#     return


# def gg_ln(n: float) -> float:
#     return


# def gg_sin(n: float) -> float:
#     return


# def gg_cos(n: float) -> float:
#     return


# def gg_tan(n: float) -> float:
#     return


# def gg_arcsin(n: float) -> float:
#     return


# def gg_arccos(n: float) -> float:
#     return


# def gg_arctan(n: float) -> float:
#     return


# def gg_sinh(n: float) -> float:
#     return


# def gg_cosh(n: float) -> float:
#     return


# def gg_tanh(n: float) -> float:
#     return


# def gg_arcsinh(n: float) -> float:
#     return


# def gg_arccosh(n: float) -> float:
#     return


# def gg_arctanh(n: float) -> float:
#     return


# def gg_csc(n: float) -> float:
#     return


# def gg_sec(n: float) -> float:
#     return


# def gg_cot(n: float) -> float:
#     return


# def gg_arccsc(n: float) -> float:
#     return


# def gg_arcsec(n: float) -> float:
#     return


# def gg_arccot(n: float) -> float:
#     return


# def gg_csch(n: float) -> float:
#     return


# def gg_sech(n: float) -> float:
#     return


# def gg_coth(n: float) -> float:
#     return


# def gg_arccsch(n: float) -> float:
#     return


# def gg_arcsech(n: float) -> float:
#     return


# def gg_arccoth(n: float) -> float:
#     return


builtins: list[Builtin] = [
    Builtin("Sqrt", ["float"], lambda n: math.sqrt(n)),
    Builtin("Root", ["float", "float"], lambda base, n: safePow(base, 1 / n)),
    Builtin("Min", ["float", "float"], lambda a, b: min(a, b)),
    Builtin("Max", ["float", "float"], lambda a, b: max(a, b)),
    Builtin("Abs", ["float"], lambda n: abs(n)),
    # Builtin("Round", ["float", "int"], lambda n, precision: round()),
]
