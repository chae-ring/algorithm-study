#bronze2
"""
Docstring for baekjoon.bronze.단어의 개수

문제 번호: 1152
URL:    https://www.acmicpc.net/problem/1152
문제: 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까?
      단어는 공백 한 칸으로 구분되며, 공백이 연속해서 나올 수 있다. 또한 문자열의 앞과 뒤에는 공백이 있을 수도 있다.
      예를 들어, 문자열 "The Curious Case of Benjamin Button"에는 6개의 단어가 있다.
입력: 첫 줄에 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열의 길이는 1,000,000을 넘지 않는다.
출력: 첫째 줄에 단어의 개수를 출력한다. 

"""
s=input()
result=s.split()
print(len(result))
