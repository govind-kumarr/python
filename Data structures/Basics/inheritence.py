class Animal:
    def __init__(self, name: str, age: int, num_legs: int) -> None:
        self.name = name
        self.age = age
        self.num_legs = num_legs

    def __repr__(self) -> str:
        return "<class 'Animal'>"

    def __str__(self) -> str:
        return f"name: {self.name}, age: {self.age}, legs:{self.num_legs}"

    def talk(self) -> None:
        print(f"{self.name} can't talk")


class Dog(Animal):
    def __init__(self, name: str, age: int, num_legs: int, breed: str) -> None:
        super().__init__(name, age, num_legs)
        self.breed = breed
        self.type = "dog"

    def __str__(self) -> str:
        return f"type: {self.type}, breed: {self.breed},"

    def talk(self) -> None:
        print(f"{self.name} can say hi")


bruno = Dog("bruno", 1, 4, "dobermenn")

bruno.talk()
