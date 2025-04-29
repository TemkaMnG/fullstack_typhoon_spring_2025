# ===============================================================
# Дасгал 4: Алдаа дамжуулах (re-raising)
# ===============================================================


def process_data(data):

    """
    Өгөгдлийг боловсруулж, алдаа гарвал дэлгэрэнгүй мэдээлэлтэйгээр дамжуулах.

    Даалгавар:
    1. data-г тоо руу хөрвүүлэх оролдлого хийх
    2. Хэрэв ValueError гарвал, алдааг барьж дэлгэрэнгүй мессежтэйгээр дахин өргөх
    """
    # Энд кодоо бичнэ үү
    try:
        dataaa = int(data)
        return dataaa
    
    except ValueError:
        raise ValueError("Bolowsruulalt amjiltgvi bolson")

def exercise_4():
    """
    Алдаа дамжуулах жишээг турших.

    Даалгавар:
    1. process_data функцийг дуудаж, алдаа барих
    2. "abc" утгыг дамжуулж, алдааг хэрхэн дамжуулж байгааг харах
    """
    # Энд кодоо бичнэ үү
    try:
        dataa = process_data(input("utga oruul: "))
        print(dataa)

    except ValueError:
        print("Utga buruu bna!")

exercise_4()
