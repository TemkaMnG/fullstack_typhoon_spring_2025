# exercise 3

file = open('sample_text.txt', 'w')
file.write("""Зааварчилгаа:
    1. Хэд хэдэн догол мөртэй текст бүхий 'sample_text.txt' нэртэй файл үүсгэнэ үү
    2. Файлыг уншиж үг бүр хэдэн удаа гарч ирснийг тоолох функцийг гүйцээнэ үү
    3. Үр дүнг давтамжаар нь эрэмбэлж хэвлэнэ үү (хамгийн их давтагдсан үгүүд эхэндээ)
    4. Том, жижиг үсгийг ялгахгүй ('Word' ба 'word'-г ижил үг гэж үзнэ)
    . Үндсэн цэг, таслалуудыг арилгана уу""")
def count_words(sample_text):
    try:
        word_counts = count_words('sample_text.txt')
        print("Үгийн давтамжууд:")
        print(word_counts, top_n=10)  # Хамгийн их давтамжтай 10 үгийг хэвлэнэ
    except FileNotFoundError:
        print("Алдаа: 'sample_text.txt' файл олдсонгүй.")
        print("Энэ програмыг ажиллуулахын өмнө текст агуулсан энэ файлыг үүсгэнэ үү.")

count_words("sample_text: count_words")