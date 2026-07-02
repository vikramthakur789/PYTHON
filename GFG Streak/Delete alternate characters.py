class Solution:
    def delAlternate (self, s):
        # code here 
        result =""
        
        for i in range(len(s)):
            if i % 2 == 0:
                result += s[i]
                
        return result        
