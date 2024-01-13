class Person:
    def __init__(self, name):
        self.name = name


def get_name(self: Person) -> str:
    return self.name


def a_class_method(cls: type):
    print(f"A class method of {cls} was called.")


def a_static_method():
    print("A static method was called.")


# Adding instance method
Person.get_name = get_name

# Adding a class method
Person.a_class_method = classmethod(a_class_method)

# Adding a static method
Person.a_static_method = staticmethod(a_static_method)


def main():
    person = Person("Jim")
    print(Person.get_name(person))
    Person.a_class_method()
    Person.a_static_method()


if __name__ == "__main__":
    main()
