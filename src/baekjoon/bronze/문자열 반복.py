#bronze 2

"""
Docstring for baekjoon.bronze.문자열 반복
문제 번호: 2675
URL:    https://www.acmicpc.net/problem/2675

문제: 문자열 S를 입력받은 후, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
입력: 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
      각 테스트 케이스는 공백으로 구분된 두 정수 R과 문자열 S로 이루어져 있다.
      R은 1보다 크거나 같고, 8보다 작거나 같은 자연수이고,
      S는 길이가 20을 넘지 않는 문자열이다.
출력: 각 테스트 케이스에 대해 P를 출력한다.
"""

num = int(input())

result=[]

for _ in range(num):
    n,s=input().split()
    n=int(n)
    text=''
    for char in s:
        text +=char*n

    result.append(text)

for res in result:
    print(res)
        

