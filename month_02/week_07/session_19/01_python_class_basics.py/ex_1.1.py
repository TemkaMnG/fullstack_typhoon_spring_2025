class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def meow(self):
        return f"Meow! I'm {self.name}"
    
mittens = Cat("Mittens", "white")
luna = Cat("Luna", "black")

print(f"Cat 1: {mittens.name}, {mittens.color}")
print(f"Cat 2 {luna.name}, {luna.color}")

print(mittens.meow())
print(luna.meow())