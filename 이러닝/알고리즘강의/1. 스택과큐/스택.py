# 파이썬에서 스택은 그냥 리스트로 구현.
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) #1325 (원래 스택이 작동하는 방식)
print(stack) # 5231(스택 작동방식과 반대)