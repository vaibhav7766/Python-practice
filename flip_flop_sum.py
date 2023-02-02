#https://codeforces.com/contest/1778/problem/A
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    l=list(map(int, input().split(' ')))
    t=0
    for i in range(n-1):
        if l[i]*l[i+1]==1 and l[i]!=1:
            t=1
            break
        elif l[i]*l[i+1]==-1:
            t=2
    if t==0:
        print(sum(l)-4)
    elif t==1:
        print(sum(l)+4)
    else:
        print(sum(l))