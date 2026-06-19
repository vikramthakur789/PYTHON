class Solution:
    def merge(self, s1, s2):
        # code here
        result=""
        
        i=0
        j=0
        
        while i < len(s1) and j < len(s2):
            result += s1[i]
            result += s2[j]
            
            i += 1
            j += 1
            
        result += s1[i:]
        result += s2[j:]
            
        return result
        
            
            
            
        
