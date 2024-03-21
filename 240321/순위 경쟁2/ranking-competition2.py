import sys

n=int(sys.stdin.readline())
dic={'A':0,'B':0}
status = 'AB'
answer=0
for i in range(n):
    c,s = map(str,sys.stdin.readline().split())
    dic[c]+=int(s)
    if dic['A']>dic['B']:
        if status!='A':
            answer+=1
        status='A'
    elif dic['A']<dic['B']:
        if status!='B':
            answer+=1
        status='B'
        
    else:
        if status!='AB':
            answer+=1
        status='AB'
print(answer)