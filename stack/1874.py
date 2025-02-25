#1874
n=int(input())
arr=[]
stack=[]
answers=[]
num=1
i=0

for _ in range(n):
    arr.append(int(input()))

while(1):
    if stack and stack[-1]==arr[i]:
        stack.pop()
        answers.append("-")
        i+=1
    else:
        if num >n:
            break
        else:
            stack.append(num)
            answers.append("+")
            num+=1
if stack:
    print("NO")
else:
    for operand in answers:
        print(operand)
    
    

