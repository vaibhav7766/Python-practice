#https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import Counter
input=sys.stdin.readline

l=[]
c=[]
n=int(input())
for i in range(n):
    s=input()
    a=len(s)
    if "\n" in s:
        s1=s[:a-1]
        l.append(s1)
    else:
        l.append(s)
d=Counter(l)
val=d.values()
print(len(set(l)))
for j in val:
    print(j,end=" ")