import sys

n=int(sys.stdin.readline())
l=[]
for i in range(n):
    a,b,c=map(str,sys.stdin.readline().split())
    l.append((a,b,c))

l.sort(key=lambda x:x[1])
for (a,b,c) in l:
    print(a,b,c)