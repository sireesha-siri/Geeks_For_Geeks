#User function Template for python3

def multiply (arr, n) : 
    #Complete the function
    r = n // 2
    s1 = sum(arr[:r])
    s2 = sum(arr[r:])
    p = s1 * s2 
    return p



#{ 
 # Driver Code Starts
#Initial Template for Python 3

    

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = multiply(arr, n)
    print(ans)
# } Driver Code Ends