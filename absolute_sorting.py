#https://codeforces.com/contest/1772/problem/D
import math

for _ in range(int(input())):
    x=0
    n=int(input())
    arr=list(map(int, input().split(' ')))
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            x=max(x,math.ceil((arr[i]+arr[i+1])/2))
    for j in range(n):
        arr[j]=abs(arr[j]-x)
    for k in range(n-1):
        if arr[k]>arr[k+1]:
            x=-1
    print(x)