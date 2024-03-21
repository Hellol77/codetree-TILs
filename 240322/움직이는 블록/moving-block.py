import sys

l=[]
n=int(sys.stdin.readline())
for i in range(n):
    block=int(sys.stdin.readline())
    l.append(block)

s=sum(l)
s=s//n
answer=0
for i in l:
    if i==s:
        continue
    elif i <s:
        answer+=abs(i-s)
    elif s<i:
        answer+=abs(i-s)
print(answer//2)