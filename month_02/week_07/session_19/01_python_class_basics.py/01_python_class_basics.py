class Dog:
    """Энгийн нохой класс"""

    pass

banhar = Dog()  # object - bodit zuil
print(banhar)

bulldog = Dog()
print(bulldog)

# ___init___ gedeg klassin punkts 
class Cat():
    def __init__(self, name, race): # class parametr
        self.name = name    # class attributes, class variables
        self.race = race

    # class function/method
    
    def meaw(self):
        return f"Meaw! I'm a {self.meaw}"

    def __str__(self):
        return f"{self.name} нь {self.race}"
    
    def __repr__(self):
        return f"Dog(name={self.name}, race={self.race})"
    
# object oriented programming buyu object handalt
whitecat = Cat("Koshka", "Marine Coon")
print(whitecat)
print(whitecat.name)

print(repr(whitecat))

moon = Cat("Muurshdee", "Vildershdee")
print(moon)
print(moon.name)
print(moon.race)
print(repr(moon))

# class function call
print(moon.meaw())
print(whitecat.meaw())

# class identities
class Hourse:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

black_hourse = Hourse("Har mori", 3)
print(black_hourse.species)
print(black_hourse.age)
print(black_hourse.name)

class Dog:
    def __init__(self, name, age):
        self.name= name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"
    
    def bark(self, sound):
        return f"{self.name} says {sound}"
    
# 2 bodit nohoi uusgeed  punktsuudiig duudaj haruulna uu

balt = Dog(name="Balt", age=5)
hartsaga = Dog("Hartsaga", age=3)

print(balt.name)
print(balt.age)
print(balt.description())
print(balt.bark("how how"))

print(hartsaga.description())
print(hartsaga.bark("Havk Havk"))

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        self.__account_number = "123456"

    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value

Tamir_account = BankAccount(" Tamir", 1000000)
Tamir_account.balance(1000)
print(Tamir_account.balance)     

# Class dotor buruu attribute ashiglah

class Dog:
  #  trick = [] # mistake use of a class variable
    def __init__(self, name):
        self.name = name
        self.tricks = []
    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog("Fido")
e = Dog("Buddy")
d.add_trick("roll over")
e.add_trick("play dead")
print(d.tricks)
print(e.tricks)