#хэрэглэгчээс тоо авдаг болгоё

num1 = input('Give me first number: ')

print(f"{num1}")

num2 = input('Give me second number: ')
print(f"{num2}")

getup = input('Give me get: ')
print(f" - + * / ")


addition = int(num1) + int(num2)
subtraction = int(num1) - int(num2)
multiplication = int(num1) * int(num2)
division = int(num1) / int(num2)

print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")