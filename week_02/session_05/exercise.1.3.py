num_1 = float(input("Та дурын тоог оруулна уу: "))
print(f"Таны оруулсан тоо: {num_1}")
character = input("Та дурын тэмдэг оруулна уу: *, /, +, -, **, //: ")
print(f"{num_1} {character} ?")
num_2 = float(input("Та дурын тоог оруулна уу: "))

if character == "**":
    result = float(num_1 ** num_2)
    print(f"{num_1} ** {num_2} = {result}")
if character == "*":
    result = float(num_1 * num_2)
    print(f"{num_1} * {num_2} = {result}")
elif character == "/":
    result = float(num_1 / num_2)
    print(f"{num_1} / {num_2} = {result}")
elif character == "//":
    result = float(num_1 // num_2)
    print(f"{num_1} // {num_2} = {result}")
elif character == "+":
    result = float(num_1 + num_2)
    print(f"{num_1} + {num_2} = {result}")
elif character == "%":
    result = float(num_1 % num_2)
    print(f"{num_1} % {num_2} = {result}")
elif character == "-":
    result = float(num_1 - num_2)
    print(f"{num_1} - {num_2} = {result}")
else:
    result = "Тэмдэгт буруу байна"
