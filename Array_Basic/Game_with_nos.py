#User function Template for python3

def game_with_number (arr,  n) : 
    #Complete the function
    r = []
    for i in range(n):
        if i == n-1:
            r.append(arr[i])
            break
        else:
            v = arr[i] ^ arr[i+1]
            r.append(v)
    return r 


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = game_with_number(arr, n);
    print(*res)




# } Driver Code Ends