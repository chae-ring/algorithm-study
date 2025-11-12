"""
문제 설명:
배열 arr에서 연속적으로 나타나는 같은 숫자는 하나만 남기고 제거한다.
남은 수들은 원래 순서를 유지해야 한다.

예시:
- [1,1,3,3,0,1,1] → [1,3,0,1]
- [4,4,4,3,3] → [4,3]

제한사항:
- 1 ≤ len(arr) ≤ 1,000,000
- 0 ≤ arr[i] ≤ 9
"""

# 내 풀이
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if answer[-1] != arr[i]:
            answer.append(arr[i])
        
    return answer

# 다른 사람 풀이 (리스트 슬라이싱 트릭)
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: 
            continue
        a.append(i)
    return a