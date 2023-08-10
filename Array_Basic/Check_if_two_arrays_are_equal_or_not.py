#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        #return: True or False
        
        #code here
        # dict_a = {}
        # dict_b = {}
        # for i in range(N):
        #     if i in dict_a:
        #         dict_a[i] += 1
        #     else:
        #         dict_a[i] = 0
                
        # for j in range(N):
        #     if j in dict_b:
        #         dict_b[j] += 1
        #     else:
        #         dict_b[j] = 0 
                
        # if dict_a.items() == dict_b.items():
        #     return True
        # else:
        #     return False
        A.sort()
        B.sort()
        if A == B:
            return True
        else:
            return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        
        A = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        ob=Solution()
        if ob.check(A,B,N):
            print(1)
        else:
            print(0)
        
                
                
# } Driver Code Ends