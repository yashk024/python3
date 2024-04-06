# Generators, Iterators, and Closures

## Table of Content

1. Generator
1. The `yield` keyword & How to build a generator
1. List Comprehension
1. The `lambda` function
1. A brief look at closures

## Generator

* generators are often called as iterators
* `range()` function, a generator (or an iterator)
* a generator returns a series of values, and in general, is (implicitly) invoked more than once
* an iterator must provide two methods
    * `__iter__()`, should return the object itself and is invoked once (needed to successfully start the iteration)
    * `__next__()`, intended to return the next value, it will be invoked by the `for`/`in` statements in order to pass through the next iteration; if there are no more values to provide, the method should raise the StopIteration exception

## The `yield` keyword & How to build a generator

*   ```py
    def fun(n):
        for i in range(n):
            yield i
    for v in fun(5):
        print(v)
    ```
*   ```py
    # generator to produce the first n powers of 2
    def powers_of_2(n):
        power = 1
        for i in range(n):
            yield power
            power *= 2

    for v in powers_of_2(8):
        print(v)
    ```
*   ```py
    # list comprehension
    def powers_of_2(n):
        power = 1
        for i in range(n):
            yield power
            power *= 2

    t = [x for x in powers_of_2(5)]
    print(t)
    ```
* `list()` function can transform a series of subsequent generator invocations into a real list.
* the context created by the `in` operator allows you to use a generator
*   ```py
    # Fibonacci number generator
    def fibonacci(n):
        p = pp = 1
        for i in range(n):
            if i in [0, 1]:
                yield 1
            else:
                n = p + pp
                pp, p = p, n
                yield n
    
    fibs = list(fibonacci(10))
    print(fibs)
    ```

## List Comprehension

*   ```py
    list_2 = [10 ** ex for ex in range(6)]
    ```
*   ```py
    the_list = []
    for x in range(10):
        # here, it's not a conditional instruction, it's an operator
        the_list.append(1 if x % 2 == 0 else 0)
    ```
*   ```py
    # using list comprehension
    the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
    ```
* one change can turn any list comprehension into a generator
*   ```py
    the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
    the_generator = (1 if x % 2 == 0 else 0 for x in range(10))
    # check the length of both using len() function
    ```

## The `lambda` function

* `lambda` function, or anonymous function
* syntax &rarr; `lambda parameters: expression`

### the `map()` function

```py
list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
```

### the `filter()` function

```py
from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)
```

## A brief look at closures

```py
def outer(par):
    loc = par

    def inner():
        return loc
    return inner

var = 1
fun = outer(var)
print(fun())
# function returned during the outer() invocation is a closure
```
```py
def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power

fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))
```
