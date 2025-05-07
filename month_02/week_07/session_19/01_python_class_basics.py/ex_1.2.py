class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def meow(self):
        return f"Meow! I'm {self.name}"
    
    def __str__(self):
        return f"{self.name} is a {self.color} cat"
    
    def __repr__(self):
        return f"Cat(name={self.name}, color={self.color})"
    
    species = "Felis catus"

    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age * 7
        

mittens = Cat("Mittens", "white")
luna = Cat("Luna", "black")

print(f"Cat 1: {mittens.name}, {mittens.color}")
print(f"Cat 2: {luna.name}, {luna.color}")

print(mittens.meow())
print(luna.meow())

# str & repr
print(mittens)
print(repr(mittens))

print(luna)
print(repr(luna))

# species
mittens = Cat("Mittens", "white", 3)
luna = Cat("Luna", "Black", 2)