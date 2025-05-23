class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"{self.name} is {self.age} years old"
    
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age) # Call parent's __init__
        self.breed = breed

    def info(self):
        # Extend the parent's info method
        basic_info = super().info()
        return f"{basic_info} and is a {self.breed}"
    

rex = Dog("Rex", 3, "German Shepherd")
print(rex.info())   # Rex is 3 years old and is a German Shepherd
print(isinstance(rex, Dog))  #True
print(isinstance(rex, Animal))  #True
print(issubclass(Dog, Animal))  #True

import math
# Exercise
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

# Rectangle gedeg class uusgeed tuuniig shape class aas udamshdag bolgooroi
# Gehdee enehvv class n zaawal height, width awah estoi
# odoo tuuniigee tegsh untsugtiin talbai bolon perimetriig olood butsaadag bolgooroi
# neg tegsh untsugt uusgej testlene uu

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle = Rectangle(5, 6)
print(rectangle.area())
print(rectangle.perimeter())

# Circle gedeg class uusgeed tuuniig Shape class aas udamshdag bolgooroi
# Gehdee enehuu class n zaawal radius awah estoi
# odoo tuuniigee toirgiin talbai bolon perimetriig olood butsaadag
# bolgooroi neg tegsh ontsugt uusgej testlene uu math sang import hiij oruulj ashiglaarai

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius**2
    
    def perimeter(self):
        import math

        return 2 * math.pi * self.radius
    
circle = Circle(5)
print(circle.area())
print(circle.perimeter())