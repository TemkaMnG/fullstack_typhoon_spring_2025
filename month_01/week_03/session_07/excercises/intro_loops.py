# python loops

fruits = ["apple", "banana", "gvzeelzgene"]

# Problem -- 100 shirheg jimsnii turul list baiwal yah we?
print(fruits[0])
print(fruits[1])  
print(fruits[2])  

# solution - loop buyu davtalt
# 1
for fruit in fruits:
    print(fruit)

# 0 - 5 hurtel (5 orohgvi)
for i in range(5):
    print(i)    # 0, 1, 2, 3, 4

# 2 - 8 hurtel 
for i in range (2, 8):
    print(i)    # 2, 3, 4, 5, 6, 7, 8

# 1 - 10 hurtel, 2 alhmaar
for i in range(1, 10, 2):
    print(i)    # 1, 3, 5, 7, 9
 # string buyu text 
message = "Python"

# Temdegt bvtneer davtah
for char in message:
    print(char)

# enumerate tooloh
fruits = ["alim", "banana", "gvzeelzgene"]

# Index bolon elementiig avah
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Todorhoi index ehlel
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

#break
for i in range(10):
    if i == 5:
        break
    print(i)    # 0, 1, 2, 3, 4

#Continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)    # 1, 3, 5, 7, 9

# break hereggvi ved else heseg ajildag

for i in range(5):
    print(i)
else:
    print("Davtalt amjilttai duuslaa!")


# break heregtei ved else heseg ajillahgvi
for i in range(5):
    if i ==3:
        break
    print(i)
else:
    print("Ene heseg ajillahgvi")

# double loop
# urjuuleh heseg
for i in range(1, 3):
    for j in range(1, 3):
        print(f"{i} x {j} = {i * j}")
        print("------")

# engiin dawtalt
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)      # [1, 4, 9, 16, 25]

# Jagsaatiin oilgolt
squares = [i ** 2 for i in range(1, 6)]
print(squares)      # [1, 4, 9, 16, 25]

# Nuhtsul jagsaaltiin oilgolt
even_squares = [i ** 2 for i in range(1, 11) if i % 2 ==0]
print(even_squares)     # [4, 16, 36, 64, 100]