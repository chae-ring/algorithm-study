#5430
import sys
import ast
from collections import deque

test_case=int(input())
answers=[]

for _ in range(test_case):
    command=input()
    n=int(input())
    input_str = input()
    numbers = deque(ast.literal_eval(input_str))
    status="good"
    reverse_count=0

    for char in command:
        if char=="R":
            reverse_count+=1
        elif numbers and char=="D":
            if reverse_count%2==0:
                numbers.popleft()
            else:
                numbers.pop()
        else:
            status="error"
            break
    if status=="good":
        if reverse_count%2==0:
            answers.append(f"[{','.join(map(str, numbers))}]") 
        else:
            numbers.reverse()
            answers.append(f"[{','.join(map(str, numbers))}]") 
    else:
        answers.append(status)

for a in answers:
    print(a)

#reverse 는 여러번 수행시, O(N^2) 이 되버린다....

