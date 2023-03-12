from typing import Callable


def hello() -> None:
    print("Helow World!")


greet: Callable[[], None] = hello

greet()


def zola(name: str) -> str:
    return f"Zola,{name}"


def goodbye(name: str) -> str:
    return f"Goodbye,{name}"


def goodmorning(name: str) -> str:
    return f"Good morning,{name}"


def universal_greeter(name: str, greeter: Callable[[str], str]) -> str:
    return greeter(name)


greet = universal_greeter("Govind", goodmorning)
print(greet)


def add_by_5(num: int) -> Callable:
    def by_5() -> int:
        return num + 5

    return by_5


print(add_by_5(5)())


add: Callable[[int, int], int] = lambda a, b: a + b
print(add(3, 2))
