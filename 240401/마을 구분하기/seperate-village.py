import sys

n=int(sys.stdin.readline())
arr=[]
answer=[]
temp=1
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))


def dfs(x,y):
    global temp
    dxs=[1,1,0,0]
    dys=[0,1,0,1]

    for xx,yy in zip(dxs,dys):
        dx=xx+x
        dy=yy+y
        if check(dx,dy):
            arr[dx][dy]=0
            temp+=1
            dfs(dx,dy)
    return temp
    

            


        

def check(x,y):
    return 0<=x<n and 0<=y<n and arr[x][y]==1

for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            arr[i][j]=0
            temp=1
            answer.append(dfs(i,j))

print(len(answer))
for i in sorted(answer):
    print(i)