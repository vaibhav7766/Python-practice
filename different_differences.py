#https://codeforces.com/contest/1772/problem/C
for _ in range(int(input())):
    j=1
    diff=1
    k,n=map(int, input().split(' '))
    for i in range(1,k+1):
        print(j,end=" ")
        if n-(j+diff)>=k-(i+1):
            j+=diff
            diff+=1
        else:
            j+=1