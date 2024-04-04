# Object Oriented Programming

## The Foundations of OOP

* procedural v/s object-oriented approach
* class hierarchies, subclass and superclass
* class v/s object (or instance)
* method v/s function
* methods and properties (or attributes)
* Inheritance
* Encapsulation
* object
    * name of the object &rarr; a noun
    * properties (or attributes) &rarr; adjectives
    * methods &rarr; verbs

## OOP: Properties

### Instance Variables
```py
class ExampleClass:
    def __init__(self, val = 1):
        self.first = val

    def set_second(self, val):
        self.second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)
```

* `example_object_1` only has the property named `first`;
* `example_object_2` has two properties: `first` and `second`;
* `example_object_3` has been enriched with a property named `third` just on the fly, outside the class's code - this is possible and fully permissible.

```py
print(example_object_1._ExampleClass__first)
```

* Making a property private is limited.

### Class Variables

```py
class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)
```

```py
class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val


print(ExampleClass.__dict__)
example_object = ExampleClass(2)

print(ExampleClass.__dict__)
print(example_object.__dict__)
```

### Checking an attribute's existence

* `hasattr()` function, expects two arguments to be passed to it:
    * the class or the object being checked;
    * the name of the property whose existence has to be reported (note: it has to be a string containing the attribute name, not the name alone)

## OOP: Methods

## OOP Fundamentals: Inheritance

* `__str__()` method, returns a string
* `issubclass()` built-in function
* `isinstance()` built-in function
* the `is` operator, it checks whether two variables refer to the same object
* `super()` function
* single inheritance
* multiple inheritance
* method overriding
* polymorphism (method overriding)
* abstract methods
* single inheritance v/s multiple inheritance
* Method Resolution Order (MRO)
* The Diamond Problem
