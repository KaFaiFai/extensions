from typing import List, TypeVar, Generic, Tuple

T = TypeVar("T")


class MyClass(Generic[T]):
    def __init__(self, value: T):
        self.value = value


def new_method(self: MyClass) -> T:
    return self.value * 2


# Monkey Patching
MyClass.new_method = new_method

# Usage
obj = MyClass(5)
print(obj.new_method())  # Output: 10
