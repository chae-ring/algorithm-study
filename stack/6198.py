#6198 - △
import sys

n = int(sys.stdin.readline())
buildings = [int(sys.stdin.readline()) for _ in range(n)]

stack = []
count = 0

for height in buildings:
    while stack and stack[-1] <= height:
        stack.pop()
    
    count += len(stack)

    stack.append(height)

print(count)


