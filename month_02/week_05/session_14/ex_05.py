# ===============================================================
# Дасгал 5: Файл боловсруулах алдаа
# ===============================================================


def safe_open_file(filename):
    """
    Файлыг аюулгүй нээх функц.

    Даалгавар:
    1. Дараах алдаануудыг зохих ёсоор барих:
       - FileNotFoundError: Файл олдохгүй үед
       - PermissionError: Файлыг нээх эрх хүрэлцэхгүй үед
       - IsADirectoryError: filename нь файл биш, хавтас байх үед
    2. Алдаа гарвал None буцаах, амжилттай бол файлын объектыг буцаах
    """
    # Энд кодоо бичнэ үү
    try:
        file = open("example.txt", "r")
        content = file.read()
        print(content)
    except FileNotFoundError:
        print("File baihgvi bolgoo!")
    except PermissionError:
        print("Permisiion bvtkve!")
    except IsADirectoryError:
        print("filename нь файл биш")
    

def exercise_5():
    """
    safe_open_file функцийг турших.

    Даалгавар:
    1. Байхгүй файл, хавтас, эрх хүрэлцэхгүй файлуудаар туршилт хийх
    2. Амжилттай нээгдсэн файлын агуулгыг хэвлэх
    """
    # Энд кодоо бичнэ үү
    pass