#11279
import sys
import heapq

n = int(sys.stdin.readline().strip())
heap = []
answers = []

for _ in range(n):
    num = int(sys.stdin.readline().strip())
    
    if num == 0:
        if heap:
            temp = -heapq.heappop(heap)
            answers.append(temp)
        else:
            answers.append(0)
    else:
        heapq.heappush(heap, -num)

sys.stdout.write("\n".join(map(str, answers)) + "\n")
