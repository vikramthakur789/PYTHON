class Solution:
    def isSubSeq(self, s1, s2):
        # code here
        i = 0
        j = 0
        while i < len(s2) and j < len(s1):
            if s2[i] == s1[j]:
                j += 1
            i += 1
            
        return j = len(s1)    
        
