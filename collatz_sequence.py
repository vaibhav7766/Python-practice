def collatz(x):
    l=[x]
    if x==1:
        print(x)
    elif x%2==0:
        l.extend(collatz(x//2))
    else:
        l.extend(collatz(3*x+1))
    return l
n=int(input())
print(collatz(n))