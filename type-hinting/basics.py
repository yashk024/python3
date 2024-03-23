######################### Type Hinting Basics #########################

mystr: str = "hello, world!"
myint: int = 24
mylist: list[int] = [1, 2, 3, 4, 5]
mylist2: list[list[str]] = [["Yash", "Kumar"], ["Hello", "World"]]
mydict: dict[str, int] = {"Yash": 1, "Kumar": 2}
myset: set[int] = {1, 2, 3}


def my_sum(a: int, b: int) -> int:
    return a + b


print(my_sum(4, 5))
# print(my_sum("4", "5"))


def greet(name: str) -> None:
    print(f"Hello, {name}! How are you?")


def print_list(l: list[int]) -> None:
    for element in l:
        print(element)


print_list([1, 2, 3, 4])
# print_list("Yash")


######################### Custom Types #########################

tcp_dict = dict[str, list[str]]

my_tcp_dict: tcp_dict = {
    "MainServer": ["1.1.1.1", "80", "yes"],
    "OtherServer": ["2.2.2.2", "99", "no"],
}


def print_tcp_dict(dt: tcp_dict) -> None:
    for key, value in dt.items():
        print("NAME", key)
        print("IP", value[0])
        print("PORT", value[1])
        print("ACTIVE", value[2])


print_tcp_dict(my_tcp_dict)
