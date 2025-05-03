# math library

a = 15
b = 7
addition_result = a + b
print(f"{a} + {b} = {addition_result}")
addition_result = a - b
print(f"{a} - {b} = {addition_result}")
addition_result = a * b
print(f"{a} * {b} = {addition_result}")
addition_result = a / b
print(f"{a} / {b} = {addition_result}")
addition_result = a // b
print(f"{a} // {b} = {addition_result}")
addition_result = a ** b
print(f"{a} ** {b} = {addition_result}")


import math

# 4 iin yzguur
yazguur = math.sqrt(4)
print(yazguur)

# floor
a = 6
b = 7

result = a/b
print(f"Result is : {result}")
print(f"Result is Floor: {math.floor(result)}")
print(f"Result is Ceil: {math.ceil(result)}")

result = 4.56867
print(f"result is : {result}")
print(f" Result is with Floor: {math.floor(result)}")
print(f" Result is with Ceil: {math.ceil(result)}")

# 25-ын квадрат язгуурыг тооцоолох
import math
sqrt_result = math.sqrt(25)
print(f"25 - ын квадрат язгуур = {sqrt_result}")

# -15-ын абсолют утгыг тооцоолох
import math
fabs_result = math.fabs(-15)
print(f"-15 - ын утгыг тооцоолох = {int(fabs_result)}")

# Тоог 2 орны нарийвчлалтай тоймлох
number = 4.56789
round_result = round(number, 2)
print(round_result)

# 4.3-ын дээд хязгаарыг тооцоолох (4.3-аас их буюу тэнцүү хамгийн бага бүхэл тоо)
import math
ceil_result = math.ceil(4.3)
print(ceil_result)

# 4.7-ын доод хязгаарыг тооцоолох (4.7-оос бага буюу тэнцүү хамгийн их бүхэл тоо)
import math
floor_result = math.floor(4.7)
print(floor_result)

# 5 факториал (5!) тооцоолох
import math
factorial_result = math.factorial(5)
print(factorial_result)

# 48 ба 18-ын хамгийн их ерөнхий хуваагчийг (ХЕХХ) тооцоолох
import math
isclm_result = math.gcd(48, 18)
print(isclm_result)

# 90 градусын синусыг тооцоолох (эхлээд радианруу хөрвүүлэх)
import math
sin_result = math.sin(math.radians(90))
print(sin_result)

# 100-ын логарифм (суурь 10)-ыг тооцоолох
import math
log_result = math.log10(100)
print(log_result)



# Аравтын системээс хоёртын системд хөрвүүлэх
decimal_num = 42
binary_num = bin(decimal_num)
print(f"{decimal_num} хоёртын системд: {binary_num}")

# Өгөгдсөн тоо
binary_str = "101010" # 42 хоёртын системд
octal_str = "52" # 42 наймтын системд
hex_str = "2A" # 42 арван зургаатын системд

# Аравтын системээс наймтын системд хөрвүүлэх
hex_num = int(binary_str, 2)
octal_num = oct(hex_num)
print(f"{binary_str} хоёртын системээс наймтын системд: {octal_num}")

decimal_number = 42  # Аравтын системийн тоо
octal_number = oct(decimal_number)  # Наймтын систем рүү хөрвүүлэх
print(octal_number)  # Гаралт: 0o52

# Аравтын системээс арван зургаатын системд хөрвүүлэх
decimal_number = 42  # Аравтын системийн тоо
hex_number = hex(decimal_number)  # Арван зургаатын систем рүү хөрвүүлэх
print(hex_number)  # Гаралт: 0x2a

# Хоёртын системээс аравтын системд
binary_str = "101010"  # Хоёртын системийн тоо
decimal_number = int(binary_str, 2)  # Аравтын систем рүү хөрвүүлэх
print(decimal_number)  # Гаралт: 42

# Наймтын системээс аравтын системд
octal_str = "52"  # Наймтын системийн тоо
decimal_number = int(octal_str, 8)  # Аравтын систем рүү хөрвүүлэх
print(decimal_number)  # Гаралт: 42

# Арван зургаатын системээс аравтын системд
hex_str = "2A"  # Арван зургаатын системийн тоо
decimal_number = int(hex_str, 16)  # Аравтын систем рүү хөрвүүлэх
print(decimal_number)  # Гаралт: 42
