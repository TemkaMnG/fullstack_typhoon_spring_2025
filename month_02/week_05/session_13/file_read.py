# File Read


# Open File

file = open('file_intro.md', 'r')
content = file.read()
print(content)
file.close()

# File modes:
# 'r' - Read (default)
# 'w' - Write ( created new file or truncates exsting )
# 'a' - Append
# 'x' - Exclusive creation
# 'b' - Binary mode
# 't' - Text mode (default)
# '+' - update (read and Write)
# 
# file read line by Line
file = open('file_intro.md', 'r')
for i in range(8):
    content = file.readline()
    print(content)
file.close()

# File read all lines
file = open('file_intro.md', 'r')
content = file.readlines()
print(content)
file.close()