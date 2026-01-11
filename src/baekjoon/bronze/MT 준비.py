# 입력
N, M = map(int, input().split())

# 최소로 필요한 박스 개수 계산
boxes = (N + M - 1) // M

# 결과 출력
print(boxes)
