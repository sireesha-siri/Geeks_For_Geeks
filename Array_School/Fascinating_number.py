#User function Template for python3
class Solution:

	def fascinating(self,n):
	    # code here
	    array = str(n) + str(n*2) + str(n*3)
        new_array = sorted(array)
        array = ['1','2','3','4','5','6','7','8','9']
        if array == new_array:
            return True
        else:
            return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input().strip())
        ob = Solution()
        ans = ob.fascinating(n)
        if ans:
            print("Fascinating")
        else:
            print("Not Fascinating")
        tc -= 1

# } Driver Code Ends