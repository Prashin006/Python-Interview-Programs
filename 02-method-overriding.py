class Animal:
    def speak(self):
        return "Animal speaks"


class Dog(Animal):
    def speak(self):
        return "Dog barks"


class Cat(Animal):
    def speak(self):
        return "Cat meows"


def animal_speaks(animal):
    return animal.speak()


animal = Animal()
dog = Dog()
cat = Cat()

print(animal_speaks(animal))
print(animal_speaks(dog))
print(animal_speaks(cat))
