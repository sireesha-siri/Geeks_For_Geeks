# Given an integer N. Find the number of digits that appear in its factorial. 
# Factorial is defined as, factorial(n) = 1*2*3*4……..*N and factorial(0) = 1.
 

# Example 1:

# Input: N = 5
# Output: 3
# Explanation: Factorial of 5 is 120.
# Number of digits in 120 is 3 (1, 2, and 0)
 

# Example 2:

# Input: N = 120
# Output: 199
# Explanation: The number of digits in
# 120! is 199

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function digitsInFactorial() that takes N as input parameter and returns number of digits in factorial of N.


# Expected Time Complexity : O(N)
# Expected Auxilliary Space : O(1)


# Constraints:
# 1 ≤ N ≤ 10^5

#User function Template for python3

class Solution:
    def digitsInFactorial(self,N):
        # code here
        if N == 0 or N == 1:
            return 1
        
        digits = 0
        for i in range(2, N + 1):
            digits += math.log10(i)
        
        return math.floor(digits) + 1





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        N=int(input())
        ob=Solution()
        print(ob.digitsInFactorial(N))
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends

# Expected Approach:
# Intuition
# The idea is to make use of these properties of log:
# Property1) For a number X, number of digits in X will be (floor(log(X)) + 1). 

# Proof:
# Let x be a positive integer with k digits. This means that:
# 10^(k-1) <= x < 10^k
# Taking logarithms base 10 of both sides, we get:
# k-1 <= log(x) < k
# Adding 1 to both sides, we get:
# k <= log(x) + 1 < k+1
# Taking the floor of both sides, we get:
# k = floor(log(x) + 1)
# Therefore, the number of digits in x is equal to floor(log(x) + 1).

# Property2) log(X * Y) = log(X) + log(Y). 
# So number of digits in N! will be:
# =>  floor(log(N!)) + 1
# => floor(log(1*2*3...*N)) + 1
# => floor(log(1)+log(2)+log(3)...+log(N)) + 1.
# Note: log used here is having base of 10.

# Implementation
# Initialize a variable 'sum' of type double with 0.
# Run a loop for j from 1 to N:
# Add log10(j) to the sum.
# Return (1+ floor(sum)) as answer.
# Let us understand it better with the help of an example:
# Input: N = 5
# log1 = 0
# log2 = 0.30103
# log3 = 0.477121
# log4 = 0.60206
# log5 = 0.69897
# log(5!) = (log1+log2+log3+log4+log5) = 2.07918
# So the number of digits in 5! is (1 + floor(2.07918)) which is 3.

# Complexity
# Time Complexity: O(N), as we are running a loop having N iterations.
# Auxiliary Space: O(1), as we are not using any extra space.