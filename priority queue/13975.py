#13975 - △
import heapq

t = int(input())
for _ in range(t):
  k = int(input())
  files = list(map(int, input().split()))
  heapq.heapify(files)
  answer = 0

  while len(files) > 1:
    temp = 0
    a = heapq.heappop(files)
    b = heapq.heappop(files)
    temp += a + b
    answer += temp
    heapq.heappush(files, temp)
  
  print(answer)




            



        
