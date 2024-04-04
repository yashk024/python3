# defining a Stack class
class Stack:

    # constructor function
    def __init__(self):
        self.__stack_list = []

    # push operation
    def push(self, val):
        self.__stack_list.append(val)

    # pop operation
    def pop(self):
        del_val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return del_val


# defining a subclass of the Stack class
class AddingStack(Stack):

    # constructor function
    def __init__(self):
        super().__init__()
        self.__sum = 0

    # modified push operation
    def push(self, val):
        self.__sum += val
        super().push(val)

    # modified pop operation
    def pop(self):
        del_val = Stack.pop(self)
        self.__sum -= del_val
        return del_val

    # new method get_sum()
    def get_sum(self):
        return self.__sum


if __name__ == "__main__":
    stk = AddingStack()  # instantiating a Stack object

    stk.push(1)
    stk.push(2)
    stk.push(3)

    print("sum =", stk.get_sum())

    print(stk.pop())
    print(stk.pop())
    print(stk.pop())

    print("sum =", stk.get_sum())
