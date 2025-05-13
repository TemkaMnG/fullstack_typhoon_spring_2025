# Animal nertei class uusgeerei. name gedeg class attribute tai baina
# speaker gedeg punktstei bna. enhvv punkts ni yu n yuch hiihgvi buguud uuniig pass
# gej temdegleerei
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# dinosaur gedeg animal object uusgene uu:
dinosaur =  Animal("Dinosaur")
print(dinosaur.name)
dinosaur.speak()

# Problem: Dog Cat gedeg animal turultei class uusgeh we: Tuhain class bolgoniig
# uursdiih n duugaar hariuldag bolgooroi.

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# cat gedeg class iig Meow gedeg bolgono uu
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# 1 muur, 1 nohoi object-uudiig uusgeed tuuniigee speak hiilgeerei.

fido = Dog("Fido")
whiskers = Cat("Whiskers")

print(fido.speak())
print(whiskers.speak())

# HUman gedeg classs uusgeed tuundee humuusiig boddog bolgono uu
# enehuu punkts n zaawal implement hiigdsen baih shaardlagatai
# odoo tuunees Mongolia, Chinese gesen 2 turliin race uusgene uu
# tegeed yridag bolgohdoo tuhain heleer ni mendchildeg bolgooroi

class Human:
    def __init__(self, name):
        self.name = name

    def think(self):
        pass

    def talk(self):
        pass

class Mongolian(Human):
    def think(self):
        return f"{self.name} speak: Sain bna uu"
    def think(self):
        return f"Mongolian {self.name} is thinking"
    
class Chinese(Human):
    def talk(self):
        return f"{self.name} speak: Ni Hao Ma!"
    
    def think(self):
        return f"Chinese Man {self.name} is thinking"
    

tami = Mongolian("Tami")
huan = Chinese("Huan")
print(tami.talk())
print(huan.talk())