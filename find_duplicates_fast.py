#https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/
class Solution:
    def duplicates(self, arr, n):
        dup = set()
        visited = [False]*(n)
        for i in range(n):
            if visited[arr[i]]:
                dup.add(arr[i])
            else:
                visited[arr[i]] = True
        if len(dup)==0:
            return [-1]
        return sorted(dup)

#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends