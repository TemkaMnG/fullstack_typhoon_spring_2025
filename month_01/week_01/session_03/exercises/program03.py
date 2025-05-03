num1 = int(input("Give me First number: "))
num2 = int(input("Give me second number: "))
operator = input("Give me operator")

addition = num1 + num2             
subtraction = num1 - num2        
multiplication = num1 * num2        
division = num1 / num2              

if operator == "+":
    print(f"{num1} + {num2} = {addition}")
elif operator == "-":
    print(f"{num1} - {num2} = {subtraction}")
elif operator == "*":
    print(f"{num1} * {num2} = {multiplication}")
elif operator == "/":
    print(f"{num1} / {num2} = {division}")
else:
    print('Ta operator oruulna uu!!')



