#https://practice.geeksforgeeks.org/contest/mega-job-a-thon-hiring-challenge-for-experienced-candidates/problems/#
#User function Template for python3

class Solution :
    def isItPossible(self,s):
        l=len(s)//2
        if len(s)%2==1:
            return 0
        elif s[:l]==s[l:]:
            return 1
        return 0

#{ 
#Driver Code Starts.

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        s = input()
        ob = Solution()
        ans = ob.isItPossible(s)
        print(ans)
        tc -= 1
#} Driver Code Ends