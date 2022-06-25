import sys
import heapq
input = sys.stdin.readline

def heapsort(iterable): # 이터러블한 객체를 넣어서
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, value) # 힙에 넣고

    for i in range(len(h)):
        result.append(heapq.heappop(h)) # 힙에서 뺀다.
    return result # 정렬된 값 도출

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

res = heapsort(arr)

for i in range(n):
    print(res[i])