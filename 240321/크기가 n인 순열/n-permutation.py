import sys

l=[]
n=int(sys.stdin.readline())
visited=[0 for i in range(n+1)]
def choose(num):
    if len(l)==n:
        print(*l)
        return
    for i in range(1,n+1):
        if visited[i]==1:
            continue
        visited[i]=1
        l.append(i)
        choose(i)
        l.pop()
        visited[i]=0
choose(0)