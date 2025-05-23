# for loop ашиглаад 10 удаа Hello World гэж хэвлэнэ үү
for i in range(10):
    print('Hello World')
    print('###########')

for i in range(10):
    print('Hello World')    # built-in function
    print('###########')

    # бид нар өөрсдөө ямар нэгэн зүйл хийдэг функц (function) тодорхойлъё
# function declaration - Функц тодорхойлох
def greeting(name):
    for i in range(2):
        print(f"Hello {name}")

# function call - Функцийг дуудах
greeting('Khangai')
greeting('Tamir')
greeting('Balt')
greeting('Buynaa')
greeting('Oyunbold')

# Олон параметртай функц
def add(a, b):
    """Хоёр тоог нэмэх.
    
    Args:
        a(int/float): Эхний тоо
        b(int/float): Хоёр дахь тоо
    Returns:
        int/float: Хоёр тооны нийлбэр
    """
    return a + b

# Функцийг дуудах
result = add(5, 3)
print(result)   # Гаралт: 8

# Гурван параметр аваад нийлбэрийг нь буцаадаг addThree гэдэг функц толдорхойлох
# addThree гэдэг функц тодорхойлох
# 3 аргумент өгөөд түүнийгээ шалгаарай

def addThree(a,b,c):
    return a + b + c
result = addThree(1, 3, 4)
print(result)
# 2 Параметр аваад түүний үржвэрийг нь буцаадаг
# multiply гэдэг функц тодорхойлох
# 2 аргументдаа утгууд өгч функцээ тестлээрэй.

def multiply(a,b):
    return a * b
result = multiply(3, 5)
print(result)

