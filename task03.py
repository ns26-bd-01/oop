class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def show_info(self) -> None:
        print(f"men {self.name}.")


p01 = Person("Ali Valiyev", 15)
p02 = Person("Gani Samiyev", 18)

p01.show_info()
p02.show_info()
