#https://www.codechef.com/problems/FORESTGA
# cook your dish here
import sys

input=sys.stdin.readline
n,w,l=map(int, input().split(" "))
h=[];r=[]
for i in range(n):
    o=list(map(int, input().split(" ")))
    h.append(o[0])
    r.append(o[1])

p,q=0,10**19
while p<=q:
    m=(p+q)//2
    sn=0
    for j in range(n):
        if h[j]+(r[j])*m>=l:
            sn+=h[j]+(r[j])*m
    if sn>=w:
        f=m
        q=m-1
    else:
        p=m+1
print(f)