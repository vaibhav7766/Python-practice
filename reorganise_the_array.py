#https://practice.geeksforgeeks.org/problems/reorganize-the-array4810/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
#User function Template for python3

def Rearrange (arr,  n) :
    s=set(arr)
    for i in range(n):
        if i in s:
            arr[i]=i
        else:
            arr[i]=-1
    return arr



#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = Rearrange(arr, n);
    print(*res)




# } Driver Code Ends