#1021
from collections import deque

n,m=map(int, input().split())
targets = list(map(int, input().split()))
arr=deque([])
count=0
for i in range(1,n+1):
    arr.append(i)
for target in targets:
    index=arr.index(target)
    if index>len(arr)-index:
        num=len(arr)-index
        count+=num
        arr.rotate(num)
    elif index<=len(arr)-index:
        count+=index
        arr.rotate(-index)
    arr.popleft()
print(count)
