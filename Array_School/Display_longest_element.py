#User function Template for python3

class Solution:
    def longest(self, names, n):
    	# code here
    	index = 0
        l = 0
        for name in names:
            if len(name) > l:
                l = len(name)
                index = names.index(name)
        return names[index] 
    	
    	


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
    	n=int(input())
    	names = []
    	for i in range(n):
    		names.append(input())
    	ob = Solution()
    	print(ob.longest(names, n))
    	
    	T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends