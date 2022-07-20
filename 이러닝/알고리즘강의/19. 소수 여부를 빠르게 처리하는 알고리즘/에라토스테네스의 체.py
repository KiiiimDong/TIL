import math

n = 1000

# 모든수가 소수인 것으로 초기화.
array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n)+1)): # 2~ 1000
    if array[i] == True:
        # 배수
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1 # 배수를 증가시키면서 배수를 제거시키는 것

# 모든 소수 출력
for i in range(2, n+1):
    if array[i]:
        print(i, end = ' ')
