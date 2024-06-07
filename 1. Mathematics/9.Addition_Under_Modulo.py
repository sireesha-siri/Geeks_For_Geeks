# Given two numbers a and b, find the sum of a and b. Since the sum can be very large, find the sum modulo 109+7.

 

# Example 1:

# Input:
# a = 9223372036854775807
# b = 9223372036854775807
# Output: 582344006
# Explanation: 
# 9223372036854775807 + 9223372036854775807 
# = 18446744073709551614.
# 18446744073709551614 mod (109+7)
# = 582344006
 

# Example 2:

# Input:
# a = 1000000007
# b = 1000000007
# Output: 0
# Explanation: 1000000007 + 1000000007 =
# (2000000014) mod (109+7) = 0
 

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function sumUnderModulo() that takes a and b as input parameters and returns sum of a and b under modulo 109+7.

 

# Expected Time Complexity : O(1)
# Expected Auxilliary Space :  O(1)

 

# Constraints:
# 1 <= a,b <= 2^63-1

#User function Template for python3

class Solution:
    def sumUnderModulo(self,a,b):
        # code here
        r = (10 ** 9) + 7
        return (a+b) % r


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a,b = map(int,input().strip().split())
        ob=Solution()
        print(ob.sumUnderModulo(a,b))

# } Driver Code Ends

# Expected Approach:
# Intuition
# The idea is to make use of the distributive property of modulo operation:
# ( a + b) % c = ( ( a % c ) + ( b % c ) ) % c.
# The reason of taking Mod is to prevent integer overflows.

# Input: a=9223372036854775807, b=9223372036854775807
# If we simply add a and b then it gives integer overflow hence first take its modulo and then multiply it by using the distributive property of the modulo operation.

# Implementation
# Initialize a variable 'M' of type int with 1000000007.
# Initialize variable 'answer' with ( (a%M) + (b%M) ) %M.
# Return answer.
# Let us understand it better with the help of an example:
# Input: a=9223372036854775807, b=9223372036854775807
# (a%M) is 291172003
# (b%M) is 291172003
# ((a%M + b%M) %M) is 582344006.

# Complexity
# Time Complexity: O(1), as we are performing simple mathematical operations having constant time complexity.
# Auxiliary Space: O(1), as we are not using any extra space.