age = int(input("Give me your age: "))

if age < 0:
    print("Age cannot ne Zero!")
elif age < 13:
    print('You are a baby')
elif age < 18:
    print("You are a teenager")
elif age < 65:
    print('You are a adult')
elif age < 100:
    print("You are a senior")
else:
    print('You are a Dinosaur')