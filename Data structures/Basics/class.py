class Person:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self) -> str:
        return '<class "Person">'

    def __str__(self) -> str:
        return f"Person: first_name: {self.first_name} last_name: {self.last_name}"

    def greet(self) -> None:
        print(f"Hello👋  {self.first_name}")


p1 = Person("Louis", "zapa")
print(p1.first_name)
print(p1.last_name)
p1.greet()

# print(f"address of p1 is {hex(id(p1))}")


class Character:
    def __init__(self, name: str, attack_power: int, life: int) -> None:
        self.name = name
        self.attack_power = attack_power
        self.life = life

    def __repr__(self) -> str:
        return '<class "Character">'

    def __str__(self) -> str:
        return (
            f"name: {self.name}, attack_power: {self.attack_power}, life: {self.life}"
        )


ironman = Character(name="ironman", life=1000, attack_power=250)
print(ironman)



