class Counter:
    def __init__(self):
        self.__value = 1

    def count_up(self):
        self.__value += 1

    def count_down(self):
        self.__value -= 1

    def __add__(self, other):
        if isinstance(other, Counter):
            return self.__value + other.__value
        raise Exception("Invalid Type!")

    def __sub__(self, other):
        return self.__value - other.__value

    # __str__ is meant for user-friendly output
    def __str__(self):
        """Automatically called when we print out the object of Counter class"""
        return f"Counter: {self.__value}"

    # __repr__ is meant for a more detailed, unambiguous output
    def __repr__(self):
        return f"Counter instance, value = {self.__value}"

    def get_value(self):
        return self.__value

    def set_value(self, val):
        self.__value = val


count1 = Counter()
count2 = Counter()

count1.count_up()
count2.count_up()
count2.count_up()
count2.count_up()

print(count1, count2)
count2.set_value(0)
print(count1, count2)
print(count1 + count2)
print(count1 - count2)
print(str(count1))
print(repr(count1))