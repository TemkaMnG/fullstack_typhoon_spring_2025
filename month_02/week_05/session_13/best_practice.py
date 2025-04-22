# File handling best practice

# Encoding

with open('data.csv', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

# Large file
with open('large_file.html', 'r') as file:
    chunk_size = 1024
    while True:
        chunk = file.read(chunk_size)
        print(chunk)
        if not chunk:
            break

# Temporary file
import tempfile

with tempfile.TemporaryFile() as temp:
    temp.write(b'Temporary data')
    temp.seek(0)
    data = temp.read()
