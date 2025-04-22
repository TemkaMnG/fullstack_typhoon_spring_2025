# Дасгал 1: Энгийн Текст Файл Уншиx

# Зааварчилгаа:
# 1. Энэ скрипттэй ижил хавтсанд 'hello.txt' гэсэн файл үүсгэнэ үү
# 2. Файлд "Hello, World!" гэж бичнэ үү
# 3. Файлын агуулгыг уншиж харуулахын тулд энэ програмыг гүйцээж бичнэ үү
# exercise 1
file = open('Hello.txt', 'w')
file.write('Hello, World!')
file.close()

def read_hello_file():
    with open('Hello.txt', 'r') as file:
        for line in file:
            print(line.rstrip())

read_hello_file()



