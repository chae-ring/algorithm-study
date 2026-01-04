#bronze 1
"""
Docstring for baekjoon.bronze.세로읽기
문제 번호: 1032
URL:    https://www.acmicpc.net/problem/1032

문제: 리눅스 운영체제에서 사용하는 파일 시스템은 대소문자를 구분하는 특징이 있다. 
입력: 첫째 줄에 파일의 개수 N(1 ≤ N ≤ 50)이 주어진다.
      둘째 줄부터 N개의 줄에 걸쳐 파일 이름이 주어진다.
      각 파일 이름은 알파벳 대문자, 소문자, 점(.)으로만 이루어져 있으며,
      길이는 1보다 크거나 같고, 50보다 작거나 같다. 모든 파일 이름의 길이는 같다.
출력: 첫째 줄에 N개의 파일 이름에서 공통으로 나타나는 부분은 그대로 출력하고,
      다른 부분은 물음표(?)로 바꾸어 출력한다.  

"""
n = int(input())
files = [input() for _ in range(n)]

result = []

for chars in zip(*files):  
    if len(set(chars)) == 1:
        result.append(chars[0])
    else:
        result.append('?')

print(''.join(result))
