#bronze 3
import sys

num=[]
for i in range(1,31):
    num.append(i)

for _ in range(28):
    num.remove(int(input()))

for n in num:
    print(n)
