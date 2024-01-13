import sys
from pathlib import Path

sys.path.append(str((Path(__file__) / ".." / "..").resolve()))
from extensions import extend


class MyClass:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        kv_list = [
            f"{k}={v}" for k, v in self.__dict__.items() if not k.startswith("_")
        ]
        repr = f"{self.__class__.__name__}({', '.join(kv_list)})"
        return repr


@extend(1)
def echo(obj, opt=MyClass("hi")):
    print(f"Echoing: {obj} and {opt}")


def _test():
    echo("hello", MyClass("bye"))
    echo(MyClass(2))


if __name__ == "__main__":
    _test()
