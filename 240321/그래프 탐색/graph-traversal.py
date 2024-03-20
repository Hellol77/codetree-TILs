import sys

n,m=map(int,sys.stdin.readline().split())

l=[[0 for i in range(n+1)]for i in range(n+1)]

for i in range(m):
    x,y=map(int,sys.stdin.readline().split())
    l[x][y]=1
visited=[False for i in range(n+1)]
answer=0
def dfs(start):
    global answer
    for i in range(1,n+1):
        if l[start][i] and not visited[i]:
            answer+=1
            visited[i]=True
            dfs(i)

dfs(1)
print(answer)