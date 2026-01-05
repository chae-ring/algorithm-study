#bronze 2

#내가 푼 방법
number=1

for _ in range(3):
    number*=int(input())

n=str(number)
result=[0]*10

for c in n:
    result[int(c)] +=1

for i in range(10):
    print(result[i])


#Counter 이용     
from collections import Counter

number = 1
for _ in range(3):
    number *= int(input())

cnt = Counter(str(number))

for i in range(10):
    print(cnt[str(i)])
