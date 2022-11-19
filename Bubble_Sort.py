def BubbleSort(a,n):
    for i in range(n-1):
        num=0
        for j in range(n-1-i):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                num+=1
        if num==0:
            return a
    return a
        
n=int(input())
l=[int(x) for x in input().split()]
print(BubbleSort(l,n))