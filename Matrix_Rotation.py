#https://codeforces.com/contest/1772/problem/B
def rotate_matrix(a):
    w=a[1][0]
    x=a[0][0]
    y=a[1][1]
    z=a[0][1]
    d=[[w,x],[y,z]]
    return d

for _ in range(int(input())):
    l=[]
    flag="NO"
    for i in range(2):
        l1=list(map(int, input().split(' ')))
        l.append(l1)
    for j in range(4):
        if l[0][0]<l[0][1] and l[1][0]<l[1][1] and l[0][0]<l[1][0] and l[0][1]<l[1][1]:
            flag="YES"
            break
        else:
            l=rotate_matrix(l)
    print(flag)