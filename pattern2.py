def pattern(n):
    for i in range(1,n+1):
        for j in range(n+1):
            if j<=n-i:
                print(" ",end=" ")
            else:
                print("*",end=" ")
        print("\n")

a=int(input())
print(pattern(a))