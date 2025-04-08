fruit_list = ["alim", "banana", "guzeelzgene", "usanvzem", "kiwi"]
for list in fruit_list:
    print(list)

for index, fruit in enumerate(fruit_list, start=0):
    print(f"{index}. {fruit}")