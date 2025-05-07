# exception handling

# problem

print('This line will print')

x = 10
y = 0

if x == 5:
    print('Hello')

print('Next line')

# Division by Zero
# print(x / y)

print('Third line')

# Undsen butets
try:
    # Aldaa garch bolzoshgvi
    result = 10 / 0
except ZeroDivisionError:
    # aldaa garval hiih uildel
    print("0 - eer huwaah bolomjgvi")

print('Fourth line')

# Олон төрлийн алдааг барих

try:
    number = int(input("Too oruulna uu: "))
    result = 10 / number
except ValueError:
    print("Zow too oruulna uu!")
except ZeroDivisionError:
    print("Tegeer huwaah bolomjgui")

print('Fifth Line')

# Hed heden aldaag neg dor bairih

try:
    number = int(input("Too oruulna uu: "))
    result = 10 / number
except (ValueError, ZeroDivisionError):
    print("Buruu orolt eswel tegeer huwaah oroldogo!")

# herwee ymar negen aldaag busdaas ylgaj chadahgvi bol
# Bvh aldaag barih (Bolgoomjtoi heregleh)

#file = open("nonexistent.txt", "r")

try:
    # ersdeltei
    file = open("nonexistent.txt", "r")
except Exception as e:
    print(f"Aldaa garlaa: {e}")

print("Sixth line")

# Aldaanii medeelel awah
try:
    x = 10 / 0
except Exception as e:
    print(f"Aldaanii turul: {type(e).__name__}")
    print(f"Aldaanii messege: {str(e)}")

# else blok - aldaa garaagvi tohioldold ajillana
try:
    number = int(input("Too oruulna uu: "))
    result = 10 / number
except ValueError:
    print("Zow too oruulna uu!")
except ZeroDivisionError:
    print("Tegeer huwaah bolomjgvi!")
else:
    # Aldaa garaagui bol ajillana
    print(f"Ur dun: {result}")

# finally blok - aldaa garsan eshees ul hamaaran ajillna:

    try:
        # ersdeltei code
        file = open("example.txt", "r")
        content = file.read()
        print(content)
    except FileNotFoundError:
        print("File oldoogvi!")
    else:
        print(f"File ner: {file.name}")
        print(f"File undes: {file.undes}")
    finally:
        # Ul hamaaran ajillana
        if 'file' in locals() and not file.closed:
            file.close()

# aldaa damjuuldax (re-raising):

try:
    x= int("Too bish")
except ValueError:
    print("ValueError bolowsruulj baina....")
    # aldaag damjuulah
    # raise

# uur aldaa uusgeh:

try:
    age = int(input("Nasaa oruulna uu: "))
    if age < 0:
        raise ValueError("Nas surug too baij bolohgvi: ")
except ValueError as e:
    if "invalid literal" in str(e):
        print("Zow too oruulna uu: ")
    else:
        print(e)

# exception chaining: ( aldaa holboh):
try:
    # anhnii aldaa
    x = int("Too bish")
except ValueError as e:
    # Shine aldaa uusgej, anhnii aldaatai holboh
 #   raise RuntimeError("Bolowsruulalt amjiltgvi bolson") from e
    print(e)


# Traceback modul  ashiglah:

import traceback

try:
    # aldaa garch bolzoshgvi kod
    1 / 0
except Exception:
    # Delgerengui traceback medeelel hewleh
    traceback.print_exc()

# Exercise divide gedeg punkts bicheed a, b gedeg parametr avdag bolgono uu
# ene huu punkts n tuhain parametruudiig too eshiig shalgaad too bish bol
# ValueError aldaa ogdog harin 0-d huwaabal ZeroValueError ogdog bailgaarai.
def devide(a, b):
    try:
        int(a)
        int(b)
        result = a / b
    except ValueError:
        print("Buruu orolt eswel tegeer huwaah oroldogo!")
    except ZeroDivisionError:
        print('Do not divide number by Zero')
    except Exception:
        print('Error occurred')
    else:
        print(result)

devide(4, 0)
devide('4', 5)
devide("hi", "hi")
