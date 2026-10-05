
# Base class
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print("Product Name:", self.name)
        print("Price:", self.price)


# Q1: Electronics class
class Electronics(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def display(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Warranty:", self.warranty)


# Q1: Clothing class
class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def display(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Size:", self.size)


# Q2: Furniture class
class Furniture(Product):
    def __init__(self, name, price, material):
        super().__init__(name, price)
        self.material = material

    def display(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Material:", self.material)


# Create objects and display details
e1 = Electronics("Laptop", 50000, "2 Years")
c1 = Clothing("T-Shirt", 800, "L")
f1 = Furniture("Table", 5000, "Wood")

print("Electronics Details:")
e1.display()

print("\nClothing Details:")
c1.display()

print("\nFurniture Details:")
f1.display()
