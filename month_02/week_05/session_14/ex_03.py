# ===============================================================
# Дасгал 3: Else ба Finally блокууд
# ===============================================================


def exercise_3():
    """
    Else ба Finally блокуудыг ашиглах.

    Даалгавар:
    1. Хэрэглэгчээс файлын нэр аваад, тэр файлыг нээж агуулгыг харуулах
    2. Хэрэв файл олдохгүй бол зохих алдааны мессеж харуулах
    3. Файл амжилттай нээгдвэл Else блокт агуулгыг хэвлэх
    4. Finally блокт "Файл хаагдлаа" гэж хэвлэх
    """
    # Энд кодоо бичнэ үү
    try:
        name = input("File iin ner oruulna uu: ")
        file = open(name, "r")
        content = file.read()
        print(content)
    except FileNotFoundError:
        print("Tani oruulsan nertei file baihgvi bna!")
    else:
        print(f"File ner: {file.name}")
        # print(f"File undes: {file.undes}")
    finally:
        if 'file' in locals() and not file.closed:
            print("Файл хаагдлаа")
            file.close()
            

exercise_3()