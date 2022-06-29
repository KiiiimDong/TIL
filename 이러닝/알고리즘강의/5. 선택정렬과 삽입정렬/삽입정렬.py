number = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(number)):
    for j in range(i, 0, -1):
        if number[j] < number[j-1]:
            number[j], number[j-1] = number[j-1], number[j]
        else: # 자신보다 작은 데이터를 만나면 그 위치에서 멈춤.
            break
print(number)