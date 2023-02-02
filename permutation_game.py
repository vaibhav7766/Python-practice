#https://codeforces.com/contest/1772/problem/E
def winner(arr,n):
    f=0;s=0;c=0
    for i in range(n):
        if arr[i]==i+1 and arr[i]!=n-i:
            f+=1
        elif arr[i]!=i+1 and arr[i]==n-i:
            s+=1
        elif arr[i]!=n-i and arr[i]!=i+1:
            c+=1
    if s+c<=f:
        return "First"
    elif f+c<s:
        return "Second"
    else:
        return "Tie"

for _ in range(int(input())):
    n=int(input())
    l=list(map(int, input().split(' ')))
    print(winner(l,n))