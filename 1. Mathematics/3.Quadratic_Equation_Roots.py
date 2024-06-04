# Given a quadratic equation in the form ax2 + bx + c. Find its roots.

# Note: Return the maximum root followed by the minimum root.

# Example 1:

# Input:
# a = 1
# b = -2
# c = 1
# Output: 1 1
# Explanation:
# Roots of equation x2-2x+1 are 1 and 1.

# Example 2:

# Input:
# a = 1
# b = -7
# c = 12
# Output: 4 3
# Explanation: Roots of equation 
# x2 - 7x + 12 are 4 and 3.
 

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function quadraticRoots() which takes a, b, c as input parameters and returns a list of two integers containing the floor value of its roots in decreasing order. If roots are imaginary, the returning list should contain only 1 integer ie -1. Always return the greatest integer smaller than or equal to the result.
# Note: If roots are imaginary, the generated output will display "Imaginary".

 

# Expected Time Complexity: O(1)
# Expected Auxiliary Space : O(1)

 

# Constraints:
# -103 <= a,b,c <= 103

#User function Template for python3

from typing import List
import math
class Solution:
    def quadraticRoots(self, a : int, b : int , c:int ) -> List[int]:
        discriminent =b*b-4*a*c
        
        if discriminent < 0:
            return [-1]
            
        solution1=(-b+math.sqrt(discriminent))/(2*a)
        solution2=(-b-math.sqrt(discriminent))/(2*a)
        
        l = [int(math.floor(solution1)), int(math.floor(solution2))]
        
        return sorted(l, reverse=True)







#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        abc = [int(x) for x in input().strip().split()]
        a = abc[0]
        b = abc[1]
        c = abc[2]
        ob = Solution()
        ans = ob.quadraticRoots(a, b, c)
        if len(ans) == 1 and ans[0] == -1:
            print("Imaginary")
        else:
            for i in range(len(ans)):
                print(ans[i], end=" ")
            print()

# } Driver Code Ends

# Expected Approach:
# Intuition
# The idea is to use Sridharacharya Formula for finding roots of quadratic equation ax2 + bx + c =0.


 
# The values of the roots depends on the term (b2 – 4ac) which is known as the discriminant (D). 
# If D > 0:
#        => This occurs when b2 > 4ac.
#        => The roots are real and unequal.
#        => The roots are {-b + √(b2 – 4ac)}/2a and {-b – √(b2 – 4ac)}/2a.
# Else If D = 0:
#        => This occurs when b2 = 4ac.
#        => The roots are real and equal.
#        => The roots are (-b/2a).
# Else if D < 0:
#        => This occurs when b2 < 4ac.
#        => The roots are imaginary and unequal.

# Implementation
# Declare empty vector 'roots' and two variables root1 and root2.
# Initialize variable temp with value (b2 – 4ac), it is the value of discriminant (D).
# If temp is less than 0, means roots are imaginary. 
# So push back -1 into 'roots' vector as asked in problem statement.
# Else roots are real, so calculate root1 and root2 using Sridharacharya Formula, then take the floor value as asked in problem statement.
#            root1 is floor((-b + sqrt(temp)) / (2 * a));
#            root2 is floor((-b - sqrt(temp)) / (2 * a));
#            1. Push back max of root1 and root2 into roots vector.
#            2. Push back min of root1 and root2 into roots vector.
# Return vector 'roots' as answer.
# Let us understand it better with the help of an example:
# Input: a = 1, b = -7, c = 12
# So the equation if 1.x2 -7.x + 12 = 0
# temp (discriminant) = (-7)2 - (4*1*12 ) = 1 
# root1 = 4 (which is floor(( 7+√1)/(2*1)) = 4)
# root2 = 3 (which is floor(( 7-√1)/(2*1)) = 3).
# roots = {4, 3}.

# Complexity
# Time Complexity: O(1), as we are performing simple mathematical and logical operations having constant time complexity.
# Auxiliary Space: O(1), as we are not using any extra space, only some variables and a vector having maximum size of 2.