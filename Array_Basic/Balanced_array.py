#User function Template for python3

class Solution:
    def minValueToBalance(self,a,n):
        #code here.
        r = n // 2
        s = sum(a[:r])
        e = sum(a[r:])
        if s > e:
            return s - e 
        else:
            return e - s


#{ 
 # Driver Code Starts
#Initial Template for Python 3





t=int(input())
for _ in range(0,t):
    n=int(input())
    a = list(map(int,input().split()))
    ob = Solution()
    ans=ob.minValueToBalance(a,n)
    print(ans)

# } Driver Code Ends