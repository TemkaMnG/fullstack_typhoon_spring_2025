num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(num_list[1:10:2])

squares = [num_list ** 2 for num_list in range(1, 10)]
print(squares)

squares = [num_list ** 2 for num_list in range(5, 10) if num_list % 2 ==0]
print(squares)
