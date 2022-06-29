number = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(number)):
    min_index = i
    for j in range(i + 1, len(number)):
        if number[min_index] > number[j]:
            min_index = j
    number[i], number[min_index] = number[min_index], number[i]
print(number)