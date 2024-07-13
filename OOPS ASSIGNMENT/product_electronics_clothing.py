class Product:
    def __init__(self, product_id, name, price, discount_percentage):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__discount_percentage = discount_percentage

    # Getter for product_id
    def get_product_id(self):
        return self.__product_id

    # Setter for product_id
    def set_product_id(self, product_id):
        self.__product_id = product_id

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for price
    def get_price(self):
        return self.__price

    # Setter for price
    def set_price(self, price):
        self.__price = price

    # Getter for discount_percentage
    def get_discount_percentage(self):
        return self.__discount_percentage

    # Setter for discount_percentage
    def set_discount_percentage(self, discount_percentage):
        self.__discount_percentage = discount_percentage

    # Protected method to calculate final price after discount
    def _calculate_final_price(self):
        return self.__price * (1 - self.__discount_percentage / 100)


class Electronics(Product):
    def __init__(self, product_id, name, price, discount_percentage, warranty_period):
        super().__init__(product_id, name, price, discount_percentage)
        self.__warranty_period = warranty_period

    # Getter for warranty_period
    def get_warranty_period(self):
        return self.__warranty_period

    # Setter for warranty_period
    def set_warranty_period(self, warranty_period):
        self.__warranty_period = warranty_period


class Clothing(Product):
    def __init__(self, product_id, name, price, discount_percentage, size, material):
        super().__init__(product_id, name, price, discount_percentage)
        self.__size = size
        self.__material = material

    # Getter for size
    def get_size(self):
        return self.__size

    # Setter for size
    def set_size(self, size):
        self.__size = size

    # Getter for material
    def get_material(self):
        return self.__material

    # Setter for material
    def set_material(self, material):
        self.__material = material


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_electronic(self, electronic):
        self.products.append(electronic)

    def add_clothing(self, clothing):
        self.products.append(clothing)

    def display_products(self):
        for product in self.products:
            print(
                f"ID: {product.get_product_id()}, Name: {product.get_name()}, Final Price: {product._calculate_final_price():.2f}")

    def calculate_total_price(self):
        total = sum(product._calculate_final_price() for product in self.products)
        total_with_tax = total * 1.10
        print(f"Total Price (including 10% tax): {total_with_tax:.2f}")

# Example usage:
shopping_cart = ShoppingCart()
electronic1 = Electronics("E001", "Smartphone", 699.99, 10, "2 years")
clothing1 = Clothing("C001", "T-Shirt", 29.99, 5, "L", "Cotton")
shopping_cart.add_electronic(electronic1)
shopping_cart.add_clothing(clothing1)
shopping_cart.display_products()
shopping_cart.calculate_total_price()
