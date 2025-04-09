# Exercise 1.2: Create a table with headers and data, and calculate the average score.
headers = ["Нэр", "Оноо"]
data = [
    ["Болд", 85],
    ["Saraa", 92],
    ["Tumur", 78]
]

dundaj_onoo = sum([row[1] for row in data]) / len(data)

print("-" * 30)
print(f"|{headers[0]:<14}|{headers[1]:<14}|")
print("-" * 30)

for row in data:
    print(f"|{row[0]:<14}|{row[1]:<14}|")
print("-" * 30)

print(f"|{'Дундаж оноо':<14}|{dundaj_onoo:<14}|")
print("-" * 30)
