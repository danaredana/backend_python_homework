class Product:
    def __init__(self, name: str, category: str, price: int) -> None:
        self.name = name
        self.category = category
        self.price = price
        self.sale = 0

    def edit_category(self, new_category: str) -> None:
        self.category = new_category

    def edit_price(self, new_price: int) -> None:
        self.price = new_price

    def set_sale(self, sale: int) -> None:
        if 0 <= sale <= 100:
            self.sale = sale

    def cancel_sale(self) -> None:
        self.sale = 0

    def get_price(self) -> float:
        # Это не тупо геттер - тут надо учесть скидку и еще то, что скидка указана в процентах
        return self.price * (1 - self.sale / 100)

    def __repr__(self) -> str:
        return f"Product(name='{self.name}', category='{self.category}', price={self.price}, sale={self.sale}%)"
