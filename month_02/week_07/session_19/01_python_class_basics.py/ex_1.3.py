    
class Cat:
    species = "Felis catus"

    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age * 7

    def change_name(self, name):
        self.name = name
        return f"{self.name}"
        
# species
# mittens = Cat("Mittens", "white", 3)
# luna = Cat("Luna", "Black", 2)
# print(mittens.species)
# print(mittens.color)
# print(mittens.age)

# print(luna.species)
# print(luna.name)
# print(luna.color)
# print(luna.age)

name = Cat("Luna")
print(name.change_name("Snowball"))