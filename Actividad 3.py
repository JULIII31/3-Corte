# Class
class Dog:
    def __init__(self, size, color, breed, price, name):
        self.size = size
        self.color = color
        self.breed = breed
        self.price = price
        self.name = name

    def walk(self):
        print(f"{self.name} is going for a walk!")

class Bird:
    def __init__(self, size, color, species, price, name):
        self.size = size
        self.color = color
        self.species = species
        self.price = price
        self.name = name

    def fly(self):
        print(f"{self.name} is flying in the sky!")

class Cat:
    def __init__(self, age, color, breed, price, name):
        self.age = age
        self.color = color
        self.breed = breed
        self.price = price
        self.name = name

    def purr(self):
        print(f"{self.name} is purring.")


Max = Dog("large", "black", "Labrador", 1000, "Max")
Buddy = Dog("medium", "brown", "Boxer", 850, "Buddy")
Luna = Dog("small", "white", "Poodle", 1200, "Luna")
Rocky = Dog("large", "gray", "Mastiff", 1500, "Rocky")
Bella = Dog("medium", "gold", "Golden Retriever", 1300, "Bella")

Max.walk()
Buddy.walk()
Luna.walk()
Rocky.walk()
Bella.walk()

Kiwi = Bird("small", "green", "Parrot", 200, "Kiwi")
Sunny = Bird("small", "yellow", "Canary", 150, "Sunny")
Sky = Bird("medium", "blue", "Macaw", 2500, "Sky")
Ruby = Bird("small", "red", "Lovebird", 300, "Ruby")
Snow = Bird("medium", "white", "Cockatoo", 1800, "Snow")

Kiwi.fly()
Sunny.fly()
Sky.fly()
Ruby.fly()
Snow.fly()

Simba = Cat(2, "orange", "Persian", 900, "Simba")
Milo = Cat(1, "gray", "Siamese", 800, "Milo")
Lily = Cat(3, "white", "Ragdoll", 1000, "Lily")
Shadow = Cat(4, "black", "Bombay", 700, "Shadow")
Chloe = Cat(2, "brown", "Maine Coon", 1200, "Chloe")

Simba.purr()
Milo.purr()
Lily.purr()
Shadow.purr()
Chloe.purr()
