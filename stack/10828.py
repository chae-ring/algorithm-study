# 10828
n=int(input())
stack=[]
answers=[]
for _ in range(n):
    command=input()
    if "push" in command:
        c,num=command.split()
        stack.append(num)
    elif "pop" in command:
        if stack:
            pop_num=stack.pop()
            answers.append(pop_num)
        else:
            answers.append(-1)
    elif "size" in command:
        answers.append(len(stack))
    elif "empty" in command:
        if stack:
            answers.append(0)
        else:
            answers.append(1)
    else:
        if stack:
            answers.append(stack[-1])
        else:
            answers.append(-1)
for a in answers:
    print(a)
            
        