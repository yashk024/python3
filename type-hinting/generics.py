from typing import TypeVar

K = TypeVar("K")
V = TypeVar("V")
T = TypeVar("T")


def find_in_dict(d: dict[K, V], v: V) -> bool:
    return v in d.values()


mydict = {"a": 1, "b": 2, "c": 3}
print(find_in_dict(mydict, 2))
