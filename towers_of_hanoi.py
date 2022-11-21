def TowerOfHanoi(n,A,B,C):           
    if n==1:
        print("Move disc 1 from pole",A,"to pole",B)
        return
    TowerOfHanoi(n-1,A,C,B)
    print("Move disc",n,"from pole",A,"to pole",B)
    TowerOfHanoi(n-1,C,B,A)

n=int(input())
TowerOfHanoi(n,'A','C','B')