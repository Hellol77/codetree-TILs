import sys

n,m=map(int,sys.stdin.readline().split())
l=[]
def choose(num):
    if len(l)==m:
        print(*l)
    for i in range(num,n+1):
        l.append(i)
        choose(i+1)
        l.pop()

    
choose(1)