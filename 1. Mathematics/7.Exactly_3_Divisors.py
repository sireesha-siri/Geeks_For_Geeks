# Given a positive integer value N. The task is to find how many numbers less than or equal to N have numbers of divisors exactly equal to 3.

 

# Example 1:

# Input:
# N = 6
# Output: 1
# Explanation: The only number less than 6 with 
# 3 divisors is 4 which has 1, 2 and 4 as divisors.
# Example 2:

# Input:
# N = 10
# Output: 2
# Explanation: 4 and 9 have 3 divisors.
 

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function exactly3Divisors() that takes N as input parameter and returns count of numbers less than or equal to N with exactly 3 divisors.

 

# Expected Time Complexity : O(N1/2 * N1/4)
# Expected Auxilliary Space :  O(1)

 

# Constraints :
# 1 <= N <= 10^9

#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


# } Driver Code Ends
#User function Template for python3

class Solution:
    def isPrime(self, n):
        # if n == 1:
        #     return False
            
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
                
        return True

    def exactly3Divisors(self, N):
        count = 0
        
        for i in range(2, int(N**0.5)+1):
            if self.isPrime(i):
                count += 1
                
        return count
            

#{ 
 # Driver Code Starts.
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        ob=Solution()
        print(ob.exactly3Divisors(N))
        
        T-=1
    

if __name__=="__main__":
    main()
# } Driver Code Ends

# Brute Force:
# Intuition:
# We can simply run a for loop from 1 to N and then for each number x we can find the number of factors and if the number of factors is 3 then we will add 1 to our answer.

# Implementation:
# Initialize an answer variable with zero to store the answer.
# Run a loop from 1 to N.
# For every ith index run another loop from 1 to i and check how many divisors are present for i.
# If the number of divisors of i is 3 then increase the answer by 1.
# Return the answer.

# class Solution {
# public:
#     bool hasThreeDivisors(int n)
#     {
#         int numberofFactors = 0;
#         for (int i = 1; i <= n; i++) {
#             if (n % i == 0)
#                 numberofFactors++;
#         }
#         return numberofFactors == 3;
#     }
#     int exactly3Divisors(int N)
#     {
#         int ans = 0;
#         for (int i = 1; i <= N; i++) {
#             if (hasThreeDivisors(i))
#                 ans++;
#         }
#         return ans;
#         // Your code here
#     }
# };
# Complexity:
# Time Complexity: O(N2) as we are running two nested for loops from 1 to N.
# Space Complexity: O(1) as we are only using variables of type int.

# Optimized Brute Force:
# Intuition:
# We can simply run a for loop from 1 to N and then for each number x we can find the number of factors and if the number of factors is 3 then we will add 1 to our answer. But this time we will use the sqrt(N) approach to find the number of factors.

# Implementation:
# Initialize an answer variable with zero to store the answer.
# Run a loop from 1 to N.
# For every ith index run another loop from 2 to sqrt(i) and check how many divisors are present for i.
# If the number of divisors of i is 3 then increase the answer by 1.
# Return the answer.

# class Solution {
# public:
#    bool hasThreeDivisors(int n)
#    {
#        int numberofFactors = 2;
#        for (int i = 2; i * i <= n; i++) {
#            if (n % i == 0) {
#                numberofFactors++;
#                if (i * i != n)
#                    numberofFactors++;
#            }
#        }
#        return numberofFactors == 3;
#    }
#    int exactly3Divisors(int N)
#    {
#        int ans = 0;
#        for (int i = 1; i <= N; i++) {
#            if (hasThreeDivisors(i))
#                ans++;
#        }
#        return ans;
#        // Your code here
#    }
# };
# Complexity:
# Time Complexity: O(N3/2) as we are running two nested for loops one from 1 to N and the other from 2 to sqrt(N).
# Space Complexity: O(1) as we are only using variables of type int.

# Expected Approach:
# Intuition:
# We can optimize the above solution by simple observation. The observation is only perfect squares of primes can have exactly three divisors.
# So we need to find all primes p such that p*p<=N. 

# Implementation:
# Run a for loop from 1 to sqrt(N).
# For each i determine if i is prime or not if i is prime then increment the answer.
# To find if i is prime or not use the sqrt(N) approach as discussed here.
# Return the answer.
# Complexity:
# Time Complexity: O(N1/2 * N1/4) as we are running two nested for loops one from 1 to sqrt(N) and the other from 1 to sqrt(sqrt(N)).
# Space Complexity: O(1) as we are only using a variable of type int in the for loop.


# #Back-end complete function Template for Python 3

# class Solution:
#     # function to check if N is prime
#     def isPrime(self,N):
#         if (N==1):
#             return False
#         for i in range(2,1+int(math.sqrt(N))):
#             if N%i==0:
#                 return False
#         return True
        
#     # function to check the numbers with exactly 3 divisors
#     def exactly3Divisors(self,N):
#         N = int(math.sqrt(N))
#         #Initializing counter to zero
#         counter=0 
#         #Running a loop from 1 to sqrt(N)
#         for i in range(1,N+1): 
        
#             # A number N only has 3 divisors if it is a  
#             # perfect square and its square  root is a prime number, 
#             # and we know the number of perfect squares less than N which 
#             # is sqrt(N), so just checking if i is prime or not
#             if(self.isPrime(i)): 
#                 counter+=1
#         return counter