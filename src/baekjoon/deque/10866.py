#10866
from collections import deque

n=int(input())
arr=deque([])
answers=[]

while(n):
    command=input()

    if "push_back" in command:
        c,num=command.split()
        arr.append(num)
    elif "push_front" in command:
        c,num=command.split()
        arr.appendleft(num)
    elif "pop_front" in command:
        if arr:
            answers.append(arr.popleft())
        else:
            answers.append(-1)
    elif "pop_back" in command:
        if arr:
            answers.append(arr.pop())
        else:
            answers.append(-1)
    elif "size" in command:
        answers.append(len(arr))
    elif "empty" in command:
        if arr:
            answers.append(0)
        else:
            answers.append(1)
    elif "front" in command:
        if arr:
            answers.append(arr[0])
        else:
            answers.append(-1)
    else:
        if arr:
            answers.append(arr[-1])
        else:
            answers.append(-1)
    n-=1
for i in answers:
    print(i)
