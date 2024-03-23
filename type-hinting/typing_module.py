from typing import Any, Sequence, Callable, Union, Optional


# Any
def myfunction(value: Any) -> Any:
    return value * 2


print(myfunction("hello"))
print(myfunction(2))
print(myfunction([1, 2]))


# Sequence
def myfunction2(seq: Sequence) -> None:
    for e in seq:
        print(e)


print([1, 2, 3, 4])
print("hello")


# Callable
def myfunction3(fun: Callable):
    fun()


def fun():
    print("hello, world")


myfunction3(fun)


# Union
def myfunction4(value: Union[str, int]) -> None:
    print(value * 2)


myfunction4(10)
myfunction4("hello")
# myfunction4([1, 2, 3])


# Optional
def myfunction5(value: Optional[int] = 5) -> None:
    print(value)


myfunction5(45)
myfunction5()
