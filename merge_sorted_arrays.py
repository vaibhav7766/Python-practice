#https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1
#User function Template for python3
import bisect

class Solution:
    
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        l=[]
        for i in range(n):
            bisect.insort(l,arr1[i])
        for j in range(m):
            bisect.insort(l,arr2[j])
        arr1[:]=l[:n]
        arr2[:]=l[n:]



#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n,m = map(int, input().strip().split())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob=Solution()
        ob.merge(arr1, arr2, n, m)
        print(*arr1,end=" ")
        print(*arr2)
# } Driver Code Ends