#https://www.codechef.com/problems/MINPIZZAS?tab=statement
# cook your dish here
def calculate_pizzas(a,b):
    if b==0:
        return a
    return calculate_pizzas(b,a%b)
for _ in range(int(input())):
    n,k=map(int,input().split(" "))
    print(n//calculate_pizzas(n,k))