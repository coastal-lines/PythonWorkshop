class Animal:
    def die(self):
        print('buy-buy')
        self.health = 0

class Carnivour:
    def hunt(self):
        print('eating')
        self.satiety = 100

class Dog(Animal, Carnivour):
    def bark(self):
        print('woof-woof')

dog = Dog()
dog.bark()
dog.hunt()
dog.die()

