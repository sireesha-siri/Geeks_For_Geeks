# Given the first 2 terms A and B of a Geometric Series. The task is to find the Nth term of the series.

# Example 1:

# Input:
# A = 2 
# B = 3
# N = 1
# Output: 2
# Explanation: The first term is already
# given in the input as 2
# Example 2:

# Input:
# A = 1
# B = 2
# N = 5
# Output: 16
# Explanation: Common ratio = 2,
# Hence Fifth term is 1*(2)(5-1) = 24 = 16 .
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function termOfGP() that takes A, B and N as parameter and returns Nth term of GP. The return value should be double that would be automatically converted to floor by the driver code.

# Expected Time Complexity : O(logN)
# Expected Auxilliary Space : O(1)

# Constraints:
# -100 <= A <= 100
# -100 <= B <= 100
# 1 <= N <= 5


#Time Complexity: O(log(n)), as we are using the pow function, if we are using modular exponentiation to calculate the power then it will take O(log(n) time. 
#Auxiliary Space: O(1) as we only used only 3 variables.

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3

class Solution:    
    #Compelte his function
    def termOfGP(self,A,B,N):
        #Your code here
        r = B / A
        p = N - 1
        term = A*(r ** p)
        return(term)


#{ 
 # Driver Code Starts.
def main():
    
    T=int(input())
    
    while(T>0):
        
        AB=[int(x) for x in input().strip().split()]
        A=AB[0]
        B=AB[1]
        
        N=int(input())
        ob=Solution()
        print(math.floor(ob.termOfGP(A,B,N)))
        
        T-=1
    
    


if __name__=="__main__":
    main()
# } Driver Code Ends

