#User function Template for python3

class Solution:
    def isSubSequence(self, A, B):
        #code here
        i = 0
        j = 0
        
        while i < len(B) and j < len(A):
            if B[i] == A[j]:
                j += 1
            i += 1
            
        return int(j == len(A))   
