import sys

x,y=map(int,sys.stdin.readline().split())
answer=0
for i in range(x,y+1):
    s=str(i)
    temp=0
    for j in s:
        temp+=int(j)

    answer=max(answer,temp)
print(answer)