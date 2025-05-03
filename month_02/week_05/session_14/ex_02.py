def exercise_2():
    try:
        a = int(input("Too oruulna uu "))
        result = a ** 2
    except ValueError:
        print("Too bish utga oruulsan bna!")
    except OverflowError:
        print("Ur dvn het ih baina!")
    # except Exception:
    #     print("Too bish utga bna!")
    else:
        print(result)

exercise_2()
