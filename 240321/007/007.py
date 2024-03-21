import sys

a1,b1,c1=map(str,sys.stdin.readline().split())

class c:
    def __init__(self,q,w,e):
        self.a=q
        self.b=w
        self.p=e

k=c(a1,b1,c1)

print('secret code :',k.a)
print('meeting point :',k.b)
print('time :',k.p)