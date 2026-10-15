"""Небольшой тестовый скрипт для проверки работы в ветке Yura."""


def greet(name: str) -> str:
    return f"Привет, {name}!"


def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print(greet("Yura"))
    print("2 + 3 =", add(2, 3))
