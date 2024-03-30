import sys

n,m=map(int,sys.stdin.readline().split())
arr=[]
visited = [[0 for i in range(n)] for i in range(m)]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

def dfs(x,y):
    
    if x==n-1 and y==m-1:
        return True
    dxs = [1,0]
    dys = [0,1]
    for i in range(2):
        dx=dxs[i]+x
        dy=dys[i]+y
        if 0<=dx<n and 0<=dy<m and arr[dx][dy] == 1 and visited[dx][dy]==0:
            visited[dx][dy]=1
            dfs(dx,dy)

if dfs(0,0):
    print(1)
else:
    print(0)