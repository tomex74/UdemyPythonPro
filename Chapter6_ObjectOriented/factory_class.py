import math

class Pizza:
    def __init__(self, radius=36.0, ingredients=['mozzarella', 'tomatoes']):
        self.radius = radius
        if self.radius < 28.0:
            self.radius = 28.0
        elif self.radius > 64.0:
            self.radius = 64.0
        self.ingredients = ingredients
        self.pizza_dough_price = 0.001
        self.ingredients_price = 1.5

    def __str__(self):
        return f'size={self.radius!r}, ingredients={self.ingredients!r}'

    def __repr__(self):
        return f'Pizza(size={self.radius!r}, ingredients={self.ingredients!r})'

    def add_ingredient(self, ingredients):
        self.ingredients.extend(ingredients)

    @classmethod
    def margherita(cls, radius=36.0):
        return cls(radius, ['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls, radius=36.0):
        return cls(radius, ['mozzarella', 'tomatoes', 'ham'])

    @classmethod
    def salami(cls, radius=36.0):
        return cls(radius, ['mozzarella', 'tomatoes', 'salami'])

    def pizza_price(self):
        vanilla_pizza_price = self.pizza_dough_price * Pizza.circle_area(self.radius)
        ingredients_price = self.ingredients_price * len(self.ingredients)
        return round(vanilla_pizza_price + ingredients_price, 2)

    @staticmethod
    def circle_area(radius):
        return (radius**2) * math.pi


if __name__ == "__main__":
    p1 = Pizza.margherita()
    p1_price = p1.pizza_price()
    print(p1, p1_price)
    p2 = Pizza.prosciutto()
    p2_price = p2.pizza_price()
    print(p2, p2_price)
    p3 = Pizza(ingredients=['mozzarella', 'tomatoes', 'salami', 'tuna'])
    p3_price = p3.pizza_price()
    print(p3, p3_price)
    p4 = Pizza.salami(radius=28.0)
    p4.add_ingredient(['tuna', 'ham'])
    p4_price = p4.pizza_price()
    print(p4, p4_price)
