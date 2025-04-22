# with context

with open('log.txt', 'r') as file:
    content = file.read()
    print(content)


# Read File line by line
with open("log.txt", 'r') as file:
    for line in file:
        print(line.rstrip())


# 