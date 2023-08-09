# Your task is to complete this function
# Function should return True/False or 1/0
def PalinArray(arr ,n):
    # Code here
    status = False
    for i in range(n):
        num = str(arr[i])
        reverse = ''
        for j in num:
            reverse = j + reverse
        if(reverse == num):
            status = True
        else:
            status = False
            break
    return status


#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr, n):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends