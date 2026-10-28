class Category:
    def __init__(self, name: str) -> None:
        self.name = name


class Product:
    def __init__(self, name: str, category: Category, price: float):
        self.name = name
        self.category = category
        self.price = price


c01 = Category("Oziq-ovqatlar")
c02 = Category("Texnikalar")

p01 = Product("Non", c01, 4500)
