#https://practice.geeksforgeeks.org/problems/-rearrange-array-alternately-1587115620/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
#User function Template for python3
class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n): 
        l=[]
        p=0
        q=n-1
        for i in range(n):
            if i%2==0:
                l.append(arr[q])
                q-=1
            else:
                l.append(arr[p])
                p+=1
        arr[:]=l
        return arr

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            ob.rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends