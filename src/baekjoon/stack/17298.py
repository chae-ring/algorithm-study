#17298-△
n = int(input())
numbers = list(map(int, input().split()))
answers = [-1] * n  
stack = []

for i in range(n):
    while stack and numbers[stack[-1]] < numbers[i]:
        idx = stack.pop()
        answers[idx] = numbers[i]
    stack.append(i)

print(*answers)

