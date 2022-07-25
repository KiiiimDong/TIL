data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1: # 0이나 1일때(1이하일때)
        result += num
    else:
        result *= num

print(result)