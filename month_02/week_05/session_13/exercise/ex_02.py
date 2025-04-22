# exercise 2
with open('output.txt', 'w') as file:
    file.write('Hello World')

def write_and_verify(text_to_write):
    with open('output.txt', 'a') as file:
        file.write(text_to_write)

write_and_verify("Энэ бол тест юм.\nPython файл боловсруулах нь чухал!\nАмжилт хүсье!")