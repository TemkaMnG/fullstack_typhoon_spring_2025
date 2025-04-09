try:
    age = int(input("Таны нас: "))
    if age < 0:
        print("Та зөвхөн эерэг тоон утга оруулна уу")
    elif age > 120:
        print("Та зөвхөн 120-с доош нас оруулна уу")
    else:
        print(f"Таны нас: {age}")
except ValueError:
    print("Та зөвхөн тоон утга оруулна уу")
