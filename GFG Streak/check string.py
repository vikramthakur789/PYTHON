class Solution:
    def check (self,s):
        # your code here
        
        for ch in s:
            if ch != s[0]:
                return False


        return True    
