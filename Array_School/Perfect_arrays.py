#User function Template for python3

class Solution:
    def IsPerfect(self,arr,n):
        #Complete the function
        r = arr[::-1]
        if arr == r:
            return 1
        else:
            return 0



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    if(ob.IsPerfect(arr,n)):
        print("PERFECT")
    else:
        print("NOT PERFECT")
    
# } Driver Code Ends