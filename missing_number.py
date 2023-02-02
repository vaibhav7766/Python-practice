#https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
#User function Template for python3


class Solution:
    def MissingNumber(self,array,n):
        return (n*(n+1)//2)-sum(array)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends