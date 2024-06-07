# You are given two numbers a and b. You need to find the multiplication of a and b under modulo M (M as 109+7).

# Example 1:

# Input:
# a = 92233720368547758
# b = 92233720368547758
# Output: 484266119
# Explanation: Multiplication of a and b 
# under modulo M will be 484266119.
# Example 2:

# Input:
# a = 1000000007
# b = 1000000007
# Output: 0
# Explanation: Multiplication of a and b
# under modulo M is 0.
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function multiplicationUnderModulo() that takes a and b as parameters and returns multiplication of a and b under modulo M.

# Expected Time Complexity : O(1)
# Expected Auxilliary Space :  O(1)

# Constraints:
# 1 <= a,b <= 263-1

#User function Template for python3

class Solution:
    def multiplicationUnderModulo(self,a,b):
        '''
        :param a: given value of a
        :param b: given value of b
        :return: Integer , sum under modulo
        '''   
        # code here
        r = (10**9) + 7
        return (a*b) % r


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a,b = map(int,input().strip().split())
        ob=Solution()
        print(ob.multiplicationUnderModulo(a,b))

# } Driver Code Ends

# Expected Approach:
# Intuition
# The idea is to make use of the distributive property of modulo operation:
# ( a * b) % c = ( ( a % c ) * ( b % c ) ) % c.
# The reason of taking Mod is to prevent integer overflows.

# Input: a=92233720368547758,  b=92233720368547758
# If we simply multiply a and b then it gives integer overflow hence first take its modulo and then multiply it by using the distributive property of the modulo operation.

# Implementation
# Initialize a variable 'M' of type int with 1000000007.
# Initialize variable 'answer' with ( (a%M) * (b%M) ) %M.
# Return answer.
# Let us understand it better with the help of an example:
# Input: a=92233720368547758,  b=92233720368547758
# (a%M) is 722911725
# (b%M) is 722911725
# ((a%M * b%M) %M) is 484266119

# Complexity
# Time Complexity: O(1), as we are performing simple mathematical operations having constant time complexity.
# Auxiliary Space: O(1), as we are not using any extra space.