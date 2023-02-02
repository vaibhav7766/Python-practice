#https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
        curr_sum=arr[0]
        start=0
        for i in range(1,n+1):
            while curr_sum>s and start<i-1:
                curr_sum-=arr[start]
                start+=1
            if curr_sum==s:
                return [start+1,i]
            elif i<n:
                curr_sum+=arr[i]
            i+=1
        return [-1]
        
           


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends