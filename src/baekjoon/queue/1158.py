#1158
from collections import deque

n,k=map(int,input().split())
arr=deque([])
answers="<"
for i in range(1,n+1):
    arr.append(i)
while(arr):
    arr.rotate(-(k-1))
    num=arr.popleft()
    if len(arr)>0:
        answers+=str(num)
        answers+=", "
    else:
        answers+=str(num)
        answers+=">"
print(answers)
