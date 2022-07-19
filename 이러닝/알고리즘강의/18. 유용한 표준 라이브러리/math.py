# 최대공약수와 최소 공배수
import math

def lcm(a, b):
    return a * b // math.gcd(a,b)

a = 21
b = 14

print(math.gcd(21, 14)) # GCD 최대공약수
print(lcm(21, 14)) # LCM 최소 공배수