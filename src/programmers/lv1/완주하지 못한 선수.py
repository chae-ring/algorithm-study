"""
문제설명: 완주하지 못한 선수
참가자 중 한 명이 완주하지 못했다. 그 사람의 이름을 찾아라.

제한사항:
- 1 ≤ 참가자 수 ≤ 100,000
- 이름은 소문자, 최대 20자
- 동명이인 가능

예시:
["leo","kiki","eden"], ["eden","kiki"] → "leo"

"""
# 내 풀이
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]


