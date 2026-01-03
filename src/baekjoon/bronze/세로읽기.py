#bronze 1

"""
Docstring for baekjoon.bronze.세로읽기
문제 번호: 10798
URL:    https://www.acmicpc.net/problem/10798

문제: 세로로 읽기
입력: 다섯 줄에 걸쳐 길이가 최대 15인 단어가 한 줄에 하나씩 주어진다.
출력: 첫째 줄에 입력된 단어들을 세로로 읽은 결과를 출력한다.
      단어의 길이가 서로 다를 수 있으므로, 가장 긴 단어의 길이에 맞춰서 나머지 단어들은 빈 칸으로 채운 후 읽는다.
      단, 빈 칸은 출력하지 않는다.  

"""

words = [input() for _ in range(5)]
max_length = max(len(word) for word in words)
result = []
for i in range(max_length):
    for word in words:
        if i < len(word):
            result.append(word[i])
print(''.join(result)) 