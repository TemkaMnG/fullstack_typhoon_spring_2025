def exercise_1(a):
    try:
        int(a)
        result = 10 / a
    except Exception:
        print('Exception error')
exercise_1(int(input("Too oruulna uu: ")))
