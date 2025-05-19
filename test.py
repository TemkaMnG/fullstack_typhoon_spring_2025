def sandwich(word):
    if len(word) != 3:
        return "Алдаа: Үг нь яг 3 үсэгтэй байх ёстой"
    return word[0] + word[2]
