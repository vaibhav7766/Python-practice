def binary_to_decimal(n):
    l=[]
    count=0
    while n>0:
        bit=n%2
        l.append(bit)
        count+=1
        n//=2
    l=l[::-1]
    return l,count
a=int(input())
print(binary_to_decimal(a))
    