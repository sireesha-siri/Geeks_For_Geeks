#User function Template for python3

class Solution:
    def findIndex (self,a, N, key ):
        #code here.
        r = []
        if key in a:
            for i in range(n):
                if a[i] == key:
                    r.append(i)
            return r[0],r[-1]            
        else:
            return -1,-1


#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    key=int(input())
    ob = Solution()
    ans=ob.findIndex(a, n, key )
    print(*ans)
    
# } Driver Code Ends