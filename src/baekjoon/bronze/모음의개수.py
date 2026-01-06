#bronze 4

result=[]

while(1):
    i=0
    line=input()
    if line == "#":
        break
    for c in line:
        if c in "aeiouAEIOU":
            i+=1
    result.append(i)

for n in result:
    print(n)
        

