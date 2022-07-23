d = [0] * 100

d[1] = 1
d[2] = 2
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2] # 점화식 그냥 그대로 쓰는 것

print(d[n])
