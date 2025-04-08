# intro into python list

# Problem - Variables 

b = 7
print(b)

#solution -List

fruits = ["apple", "banana", "watermelon"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]
empty_list = []

print(type(fruits))
print(fruits)


# List index
# eyreg index

print(fruits[0])    # apple
print(fruits[1])    # banana
print(fruits[2])    # watermelon

# sorog index

print(fruits[-1])    # watermelon
print(fruits[-2])    # banana
print(fruits[-3])    # apple

# element change list
fruits[0] = "Vzem"
print(fruits)

# element nemeh
fruits.append("kiwi")
print(fruits)

# Todorhoi bairlald element oruulah
fruits.insert(1, "mango")
print(fruits)

# element ustgah
fruits.remove("banana")
print(fruits)

# indexeer element ustgah
removed_fruit = fruits.pop(1)
print(removed_fruit)
print(fruits)

# Bvh element ustgah
#fruits.clear()
#print(fruits)

# List methods
print(len(fruits))

# Jagsaaltiin erembe
fruits.sort()
print(fruits)

# Jagsaaltiig urvuu erembel
fruits.reverse()
print(fruits)

# elementiin index oloh
print(fruits.count("mango"))

# elementiin toog tooloh
print(fruits.count("mango"))

# Jagsaaltiig huulah
fruits_copy = fruits.copy()
print(fruits_copy)

# Jagsaaltiig negtgeh
more_fruits = ["kivi", "mango"]
fruits.extend(more_fruits)
print(fruits)

# List slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7]

#ehlel tugsgul
print(numbers[2:5])

#ehlelees tugsgul hurtel
print(numbers[:5])

# ehlelees jagsaaltiin tugsgul hurtel
print(numbers[5:])

# alham todorhoiloh
print(numbers[1:9:2])

# Jagsaaltiig huulbarlah
numbers_copy = numbers[:]
