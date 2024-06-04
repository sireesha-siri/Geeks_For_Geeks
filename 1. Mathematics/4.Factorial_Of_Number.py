# Given a positive integer N. The task is to find factorial of N.

# Example 1:

# Input:
# N = 4
# Output: 24
# Explanation: 4! = 4 * 3 * 2 * 1 = 24
# Example 2:

# Input:
# N = 13
# Output: 6227020800
# Explanation: 
# 13! = 13 * 12 * .. * 1 = 6227020800
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function factorial() that takes N as parameter and returns factorial of N.

# Expected Time Complexity : O(N)
# Expected Auxilliary Space : O(1)

# Constraints:
# 0 <= N <= 18

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3

class Solution:
    #You need to complete this function
    def factorial(self,N):
        #Your code here
        factorial = 1
        
        for i in range(2, N+1):
            factorial *= i
            
        return factorial


#{ 
 # Driver Code Starts.

def main():
    
    T=int(input())
    
    while(T>0):
        N=int(input())
        ob=Solution()
        
        print(ob.factorial(N))
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
# } Driver Code Ends