# bronze 2
"""
Docstring for baekjoon.bronze.세로읽기
문제 번호: 2587
URL:    https://www.acmicpc.net/problem/2587   

문제: 다섯 개의 자연수를 입력받아, 그 수들의 평균과 중앙값을 출력하는 프로그램을 작성하시오.
입력: 첫째 줄부터 다섯 번째 줄까지 한 줄에 하나의 자연
        수가 주어진다. 주어지는 자연수는 100보다 작거나 같다.
출력: 첫째 줄에는 다섯 개의 자연수의 평균을, 둘째 줄에는 다섯 개의 자연수를
        증가하는 순서로 정렬했을 때, 그 중앙값을 출력한다.

"""
input = [int(input()) for _ in range(5)]
input.sort()
average = sum(input) // 5
median = input[2]
print(average)
print(median)