import cmath
import math
from collections.abc import Callable
from dataclasses import dataclass
from typing import Literal

from ggraph.errors import InterpreterError

type ArgType = Literal["float", "int"]


@dataclass
class Builtin:
    name: str
    typed_impl: (
        tuple[Literal["float->float"], Callable[[float], float]]
        | tuple[Literal["float,float->float"], Callable[[float, float], float]]
        | tuple[Literal["float,int->float"], Callable[[float, int], float]]
        | tuple[Literal["int,int->float"], Callable[[int, int], float]]
        | tuple[Literal["complex->float"], Callable[[complex], float]]
        | tuple[
            Literal["complex,complex->complex"],
            Callable[[complex, complex], complex],
        ]
    )


def safePow(base: complex, power: complex) -> complex:
    ans = base**power
    if isinstance(ans, (int, float, complex)):
        return ans
    raise InterpreterError("Invalid arguments to pow")


def gg_sqrt(n: float) -> float:
    return math.sqrt(n)


def gg_root(power: complex, base: complex) -> complex:
    return safePow(base, 1.0 / power)


def gg_min(a: float, b: float) -> float:
    return min(a, b)


def gg_max(a: float, b: float) -> float:
    return max(a, b)


def gg_abs(n: float) -> float:
    return abs(n)


def gg_round(n: float, precision: int) -> float:
    return round(n, 0)


def gg_int(n: float) -> int:
    return int(n)


def gg_truncate(n: float) -> float:
    return math.trunc(n)


def gg_lcm(a: int, b: int) -> int:
    return math.lcm(a, b)


def gg_gcd(a: int, b: int) -> int:
    return math.gcd(a, b)


def gg_npr(n: int, r: int) -> int:
    return math.comb(n, r)


def gg_ncr(n: int, r: int) -> int:
    return math.perm(n, r)


def gg_exp(n: float) -> float:
    return math.exp(n)


def gg_log(n: float) -> float:
    return math.log10(n)


def gg_ln(n: float) -> float:
    return math.log(n)


def gg_sin(n: float) -> float:
    return math.sin(n)


def gg_cos(n: float) -> float:
    return math.cos(n)


def gg_tan(n: float) -> float:
    return math.tan(n)


def gg_arcsin(n: float) -> float:
    return math.asinh(n)


def gg_arccos(n: float) -> float:
    return math.acos(n)


def gg_arctan(n: float) -> float:
    return math.atan(n)


def gg_sinh(n: float) -> float:
    return math.sinh(n)


def gg_cosh(n: float) -> float:
    return math.cosh(n)


def gg_tanh(n: float) -> float:
    return math.tanh(n)


def gg_arcsinh(n: float) -> float:
    return math.asinh(n)


def gg_arccosh(n: float) -> float:
    return math.acosh(n)


def gg_arctanh(n: float) -> float:
    return math.atanh(n)


def gg_csc(n: float) -> float:
    return 1.0 / math.sin(n)


def gg_sec(n: float) -> float:
    return 1.0 / math.cos(n)


def gg_cot(n: float) -> float:
    return 1.0 / math.tan(n)


def gg_arccsc(n: float) -> float:
    return math.asin(1.0 / n)


def gg_arcsec(n: float) -> float:
    return math.acos(1.0 / n)


def gg_arccot(n: float) -> float:
    return math.atan(1.0 / n)


def gg_csch(n: float) -> float:
    return 1.0 / math.sinh(n)


def gg_sech(n: float) -> float:
    return 1.0 / math.cosh(n)


def gg_coth(n: float) -> float:
    return 1.0 / math.tanh(n)


def gg_arccsch(n: float) -> float:
    return math.asinh(1.0 / n)


def gg_arcsech(n: float) -> float:
    return math.acosh(1.0 / n)


def gg_arccoth(n: float) -> float:
    return math.atanh(1.0 / n)


def gg_mag(z: complex) -> float:
    return abs(z)


def gg_arg(z: complex) -> float:
    return cmath.phase(z) % (2 * math.pi)


builtins: list[Builtin] = [
    Builtin("Sqrt", ("float->float", gg_sqrt)),
    Builtin("Root", ("complex,complex->complex", gg_root)),
    Builtin("Min", ("float,float->float", gg_min)),
    Builtin("Max", ("float,float->float", gg_max)),
    Builtin("Abs", ("float->float", gg_abs)),
    Builtin("Round", ("float,int->float", gg_round)),
    Builtin("Int", ("float->float", gg_int)),
    Builtin("Truncate", ("float->float", gg_truncate)),
    Builtin("Lcm", ("int,int->float", gg_lcm)),
    Builtin("Gcd", ("int,int->float", gg_gcd)),
    Builtin("Npr", ("int,int->float", gg_npr)),
    Builtin("Ncr", ("int,int->float", gg_ncr)),
    Builtin("Exp", ("float->float", gg_exp)),
    Builtin("Log", ("float->float", gg_log)),
    Builtin("Ln", ("float->float", gg_ln)),
    Builtin("Sin", ("float->float", gg_sin)),
    Builtin("Cos", ("float->float", gg_cos)),
    Builtin("Tan", ("float->float", gg_tan)),
    Builtin("Arcsin", ("float->float", gg_arcsin)),
    Builtin("Arccos", ("float->float", gg_arccos)),
    Builtin("Arctan", ("float->float", gg_arctan)),
    Builtin("Sinh", ("float->float", gg_sinh)),
    Builtin("Cosh", ("float->float", gg_cosh)),
    Builtin("Tanh", ("float->float", gg_tanh)),
    Builtin("Arcsinh", ("float->float", gg_arcsinh)),
    Builtin("Arccosh", ("float->float", gg_arccosh)),
    Builtin("Arctanh", ("float->float", gg_arctanh)),
    Builtin("Csc", ("float->float", gg_csc)),
    Builtin("Sec", ("float->float", gg_sec)),
    Builtin("Cot", ("float->float", gg_cot)),
    Builtin("Arccsc", ("float->float", gg_arccsc)),
    Builtin("Arcsec", ("float->float", gg_arcsec)),
    Builtin("Arccot", ("float->float", gg_arccot)),
    Builtin("Csch", ("float->float", gg_csch)),
    Builtin("Sech", ("float->float", gg_sech)),
    Builtin("Coth", ("float->float", gg_coth)),
    Builtin("Arccsch", ("float->float", gg_arccsch)),
    Builtin("Arcsech", ("float->float", gg_arcsech)),
    Builtin("Arccoth", ("float->float", gg_arccoth)),
    Builtin("Mag", ("complex->float", gg_mag)),
    Builtin("Arg", ("complex->float", gg_arg)),
]


def construct_builtin_map() -> dict[str, Builtin]:
    res = {}
    for builtin in builtins:
        res[builtin.name] = builtin

    return res
