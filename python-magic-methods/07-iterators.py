from time import sleep


class Countdown:
    """A simple iterator that counts down from a given number"""
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        """Returns the iterator object itself."""
        return self

    def __next__(self):
        """Returns the next value in the countdown"""
        if self.current > 0:
            value = self.current
            self.current -= 1
            sleep(1)
            return value
        else:
            raise StopIteration

for num in Countdown(5):
    print(num)
# The above for loop works as follows:
# First it calls the __iter__(Countdown(5)) -> Countdown(5) which returns self
# Then it calls __next__(Countdown(5)) -> 5
# Then it calls __next__(Countdown(5)) -> 4
# Then it calls __next__(Countdown(5)) -> 3
# Then it calls __next__(Countdown(5)) -> 2
# Then it calls __next__(Countdown(5)) -> 2
# Then it calls __next__(Countdown(5)) -> 1
# Then it calls __next__(Countdown(5)) -> raise StopIteration
