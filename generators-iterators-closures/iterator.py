class Fibonacci:
    def __init__(self, n):
        self.__n = n
        self.__i = 0
        self.__f1 = self.__f2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        curr = self.__f1
        self.__f1 = self.__f2
        self.__f2 += curr
        return curr


if __name__ == "__main__":
    for i in Fibonacci(10):
        print(i, end=" ")
