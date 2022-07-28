# N개의 정수로 구성된 수열
# M개의 쿼리정보 (Left, Right), [Left,Right] 구간에 포함된 데이터들의 합을 출력
# O(N+M)
# Prefix Sum 활용

n = 5
data = [10, 20, 30, 40, 50]

# Prefix Sum 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)


left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])