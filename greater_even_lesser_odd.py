#https://practice.geeksforgeeks.org/problems/rearrange-array-such-that-even-positioned-are-greater-than-odd4804/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
#User function Template for python3

class Solution:
    def assign (self, arr,  n) : 
        l=[]
        p=0
        q=n-1
        arr.sort()
        for i in range(n):
            if (i+1)%2==0:
                l.append(arr[q])
                q-=1
            else:
                l.append(arr[p])
                p+=1
        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

  
def checkOrder(res):
    for i in range(len(res)):
        if(i%2 != 0):
            if(res[i] < res[i-1]):
                return False
        else:
            if(res[i] > res[i-1]):
                return False
    return True
for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    res = ob.assign(arr, n)
    if(checkOrder(res)):
        print("Correct")
    else:
        print("Wrong Answer")



# } Driver Code Ends