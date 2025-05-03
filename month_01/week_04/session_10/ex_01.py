# Python strings

single_quotes = 'This is single quotation text'
double_quotes = "This is double quotation text"
multi_line_string = """
                Multi Line String
                text
            """

# special characters
special_chars = "New Line: \n\tTabulator"
print(special_chars)

# raw string
special_chars = r"New Line: \n\tTabulator"
print(special_chars)

text = "Монгол"
# Индексээр хандах
print(text[0])  #M
print(text[-1]) #л

# Хэсэгчлэх хандах
print(text[0:3]) #Мон
print(text[:3]) #Мон
print(text[3:]) #гол
print(text[::-1]) #логноМ

text = "Монгол улс"
# Урт
print(len(text))  #10

# Хэсэгчлэх хандах
print(text.upper()) #МОНГОЛ УЛС
print(text.lower()) #монгол улс
print(text.capitalize()) #Монгол улс
print(text.title()) # Монгол Улс

# Хайх
print(text.find("гол")) # 3
print(text.find("орос")) # -1 олдоогүй
print("гол" in text) # True
print(text.count("о")) # 2

# Орчуулах
print(text.replace("улс", "хэл")) # Монгол хэл
# temdegt muriig huwaah
words = text.split(" ")
print(words)    # ["Монгол", Улс]

# Temdegt murvvd negtgeh
joined = ", ".join(words)
print(joined)   # Монгол, Улс

# Эхлэл, Төгсгл шалгах
print(text.startswith("Мон"))   # True
print(text.endswith("Улс"))     # true

# hooson zai arilgah
padded = " Монгол "
print(padded.strip())   # "Mongol"
print(padded.lstrip())   # "Mongol"
print(padded.rstrip())   #  "Mongol"

# temdegt muriin butets shalgah
print("123".isdigit())   # "True"
print("asd".isalpha())   # "True"
print("abc123".isalnum())   # True
print(" ".isspace())   # True

# % operator ashiglah (huuchin arga)
name = "bat"
age = 25
print("sain uu, %s! Tanii nas %d." % (name, age))
# format() arga ashiglah
print("sain uu, {}! Tanii nas {}.".format(name, age))
print("sain uu, {0}! Tanii nas {1}.".format(name, age))
print(
    "sain uu, {name}! Tanii nas {age}.".format(name=name, age=age)
    )

print("sain uu, {name}! Tanii nas {age}.")
print(f" tanii 5 jiliin daraah nas: {age + 5}")

# Toonuudiig formatlah
pi = 3.14159
print(f"pi too: {pi:.2f}") # pi too: 3.14
print(f"huwi: {0.25:.1%}")  # huwi: 25.0%

first = "Mongol"
last = "Uls"
# + operator ashiglah
full = first + " " + last
print(full) # mongol uls
message = "sain uu, "
message += "Bat!"
print(message)  # sain uu, Bat!

# olon temdegt moriig negtgeh
word = ["Python", "Hel", "surah", "hylbar"]
sentence = " ".join(words)
print(sentence) # Python hel surah hylbar

# temdegt muriig oilgolt
text = "Hello, World!"
# list comprehension
vowels = [char for char in text if char.lower() in "aeiou"]
print(vowels)   # ['e', 'o', 'o']
# temdegt muriin hurwvvleh
uppercase = [char.upper() for char in text]
print(uppercase)    # ['H E L L O    W O R L D !]