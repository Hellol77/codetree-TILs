import sys

n=int(sys.stdin.readline())
l=[]

for i in range(n):
    x,y=map(int,sys.stdin.readline().split())
    l.append((x,y))
answer=sys.maxsize


for i in range(n):
    minx=40001
    miny=40001
    maxx=-1
    maxy=-1
    for j in range(n):
        if i==j:
            continue
        minx=min(minx,l[j][0])
        miny=min(miny,l[j][1])
        maxx=max(maxx,l[j][0])
        maxy=max(maxy,l[j][1])

    answer=min(answer,abs(minx-maxx)*abs(miny-maxy))
print(answer)