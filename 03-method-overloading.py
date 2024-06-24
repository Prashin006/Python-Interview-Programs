class Maths:
    def sum(self, a, b):
        return a + b

    # The Python interpreter stores the latest definition of the function rather than storing both
    def sum(self, a, b, c):
        return a + b + c


math = Maths()
# print(math.sum(1, 2))  # causes TypeError
# print(math.sum(1, 2, 3))  # works fine. Prints 6


# So as to perform method overloading use *args and **kwargs


class Mathematics:
    def sum(self, *args):
        total = 0
        for num in args:
            total += num
        return total


mathematic = Mathematics()
print(mathematic.sum(1, 2))
print(mathematic.sum(1, 2, 3))
print(mathematic.sum(1, 2, 3, 5))
