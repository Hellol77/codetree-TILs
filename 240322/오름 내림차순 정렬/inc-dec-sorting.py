import sys

n=int(sys.stdin.readline())
l=list(map(int,sys.stdin.readline().split()))
l.sort()

print(*l)
print(*list(reversed(l)))