#https://codeforces.com/contest/1775/problem/A2
def solve(s):
    n=len(s)
    if s[:2]=="aa" or s[:2]=="bb" or s[:2]=="ba":
        a,b,c=s[0],s[1],s[2:]
        return a,b,c
    else:
        x=s.find("a",2,n)
        if x==-1:
            a,b,c=s[:n-2],s[n-2],s[n-1]
            return a,b,c
        else:
            a,b,c=s[0],s[1:x],s[x:]
            return a,b,c

for _ in range(int(input())):
    st=input()
    x,y,z=solve(st)
    print(x,y,z)