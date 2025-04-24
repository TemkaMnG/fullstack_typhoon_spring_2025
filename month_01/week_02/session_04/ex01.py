name = "John"           #string
age = 25                # integer
height = 1.75           # float, double
is_student = True       # boolean

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


# олон хувьсагчид ижил утга оноох
x = y = z = 0
print(x, y, z)

# олон хувьсагчид өөр өөр утга оноох
a, b, c = 1, 2, 3
print(a, b, c)

# Цуглуулгыг задлах
coordinates = (3, 4)
x, y = coordinates
print(x, y)

# Хувьсагчдыг солих
a, b, = 5, 10
a, b = b, a
print(a, b)

# төрөл хөрвүүлэх
float_number = float(10)    # 10.0
integer = int(3.14)         # 3
string_number = str(42)     # "42"

print(type(float_number))   # <class 'float'>
print(type(integer))        # <class 'int'>
print(type(string_number))  # <class 'str'>

is_active = True
is_completed = False

# And logic 2 утга 2 уулаа үнэн үед байдаг
print(False and False)
print(False and True)
print(True and False)
print(True and True)

# OR logic али нэг утга нь үнэн байвал үнэн болдог тэр тохиолдолыг 
print(False or False)
print(True or False)
print(False or True)
print(True or True)

# NOT logic тухайн boolean утгын эсрэг
print(not False)
print(not True)

# Жагсаалт үүсгэх
fruits = ["алим", "банана", "интоор"]
mixed_list = [1, "сайн байна", 3.14, True]

# Элементүүд рүү хандах
first_fruit = fruits[0]         # "алим"
last_fruit = fruits[-1]         # "интоор"

# Жагсаалтыг өөрчлөх
fruits.append("Улаан лооль")    # Төгсгөлд нэмэх
fruits.insert(1, "манго")       # Тодорхой байрлалд оруулах
fruits.remove("банана")         # Утгаар нь хасах
fruits_fruit = fruits.pop()     # сүүлийн элементийг хасаж буцаах

# Жагсаалтын хэсэгчлэл
numbers = [0, 1, 2, 3, 4, 5]    # 
subset = numbers[1:4]           # [1, 2, 3]

# хязгаар үүсгэх
numbers = range(5)
print(numbers)

# range(эхлэл, төгсгөл)
numbers = range(2, 7)
print(numbers)

# range(эхлэл, төгсгөл, алхам)
even_numbers = range(0, 10, 2)

# хязгаарыг жагсаалт болгох
numbers_list = list(range(5))
print(numbers_list)


x = 10 # үндсэн оноолт

# Нийлмэл оноолт
x += 5      # x = x + 5 (15)
x -= 3      # x = x - 3 (12)
x *= 2      # x = x * 2 (24)
x /= 4      # x = x / 4 (6.0)
x //= 2     # x = x // 2 (3.0)
x %= 2      # x = x % 2 (1.0)
x **= 3     # x = x ** (1.0)
print(x)

a = 10
b = 5

equal = a == b          # False
not_equal = a !=b       # True
greater_than = a > b    # Ture
less_than = a < b       # False
greater_equal = a >= b  # True
less_equal = a <= b     # False

# Гинжин харьцуулалт
result = 1 < 3 < 5      # True (1 < 3 and 3 < 5 гэсэн адил)
result = 5 > 3 < 1      # False (5 > 3 and 3 < 1 гэсэнтэй адил)