class InventoryItem:
    """A class to demonstrate operator overloading for inventory management"""
    def __init__(self, name, quantity):
        self.__name = name
        self.__quantity = quantity

    def __repr__(self):
        return f"InventoryItem(name='{self.get_name()}', quantity='{self.get_quantity()}')"

    # Arithmetic operations
    def __add__(self, other):
        if isinstance(other, InventoryItem) and self.get_name() == other.get_name():
            return InventoryItem(self.get_name(), self.get_quantity() + other.get_quantity())
        raise ValueError("Cannot add items of different types!")

    def __sub__(self, other):
        if isinstance(other, InventoryItem) and self.__name == other.__name:
            if self.get_quantity() >= other.get_quantity():
                return InventoryItem(self.get_name(), self.get_quantity() - other.get_quantity())
            raise ValueError("Cannot subtract more than the available quantity!")
        raise ValueError("Cannot subtract items of different types!")

    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            return InventoryItem(self.get_name(), int(self.get_quantity() * factor))
        raise ValueError("Multiplication factor must be a number!")

    def __truediv__(self, factor):
        if isinstance(factor, (int, float)) and factor != 0:
            return InventoryItem(self.get_name(), int(self.get_quantity() / factor))
        raise ValueError("Division factor must be a valid non-zero number!")

    # Comparison operations
    def __eq__(self, other):
        if isinstance(other, InventoryItem):
            return self.get_name() == other.get_name() and self.get_quantity() == other.get_quantity()
        raise ValueError("Quantity to be compared must be of the type 'InventoryItem'!")

    def __ne__(self, other):
        if isinstance(other, InventoryItem):
            return self.get_name() != other.get_name() or self.get_quantity() != other.get_quantity()
        raise ValueError("Quantity to be compared must be of the type 'InventoryItem'!")

    def __lt__(self, other):
        if isinstance(other, InventoryItem) and self.get_name() == other.get_name():
            return self.get_quantity() < other.get_quantity()
        raise ValueError("Cannot compare items of different types!")

    def __gt__(self, other):
        if isinstance(other, InventoryItem) and self.get_name() == other.get_name():
            return self.get_quantity() > other.get_quantity()
        raise ValueError("Cannot compare items of different types!")

    def get_name(self):
        return self.__name

    def get_quantity(self):
        return self.__quantity



item1 = InventoryItem('Tea', 10)
item2 = InventoryItem('Coffee', 25)
item3 = InventoryItem('Tea', 35)
new_item = item1 + item3

print(new_item.get_name(), new_item.get_quantity(), sep=": ")
print(item3 - item1)

result_mul = item2 * 2
print(result_mul)
print(result_mul.get_name(), result_mul.get_quantity(), sep=": ")

print(item3 > new_item)
print(item3 == InventoryItem('Tea', 35))

# Try to divide different items
try:
    result_invalid = item2 - item1
except ValueError as e:
    print(e)

# Trying to subtract more than available quantity
try:
    result_invalid = item1 - item3
    print(result_invalid.get_name(), result_invalid.get_quantity(), sep=": ")
except ValueError as e:
    print(e)
except Exception as e:
    print(e)

print(item1 != item2)
