# python tuples

# list [ 1, 2, 3, 4, 5]

# tuples
tuple1 = (1, 2, 3, 4, 5) # tuples with bracket
tuple2 = 1, 2, 3, 4, 5  # tuples without bracket
tuple3 = (1, )  # only one elemet tuple
empty_tuple = ()    #empty tuple
mixed_tuple = (1, "hoer", 3.0, True)    # multi type tuple

list_to_tuple = tuple([1, 2, 3]) # from list into tuple

# tuple access
print(tuple1[0])    # 1
print(tuple1[-1])   # 5
print(tuple1[1:3])  # (2, 3)


# tuple functions
print(tuple1.count(2))  # 1
print(tuple1.index(3))  # 2
print(len(tuple1))  # 5

print(3 in tuple1)  # True
print(6 in tuple1)  # False

tuple2 = (6, 7, 8)
combined = tuple1 + tuple2
print(combined)     # (1, 2, 3, 4, 5, 6, 7, 8,)

repeated = tuple1 * 2
print(repeated)     # (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)


# задлах tuple
person = ("bat", 25, "Ulaanbaatar")
name, age, city = person
print(name) #bat
print(age)  #25
print(city) # ulaanbatar

# swap hiih
a, b = 10, 20
a, b = b, a
print(a, b) # 20, 10

# urgutgusun zadlah
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(first)    # 1
print(middle)   # [2, 3, 4]
print(last)     # 5

tuple1 = (1, 2, 3, 4, 5)

# element uurchluh - aldaa garna
# tuple1[0] = 10    # 
# element nemeh - aldaa gargana
# tuple.appned(6)

# element ustgah
# del tuple1[0]

# to change the tuple
tuple1 = (1, 2, 3, 4, 5)
list1 = list(tuple1)
list1[0] = 10
tuple1 = tuple(list1)
print(tuple1)   # (10, 2, 3, 4, 5)
