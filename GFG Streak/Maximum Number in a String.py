class Solution:
    def extractMaximum(self, s): 
        # code here
        num = ""
        maxi = -1
        
        for ch in s:
            if ch.isdigit():
                num += ch
                
            else:
                if num != "":
                    maxi = max(maxi, int(num))
                    num = ""
                    
        # last number check
        if num != "":
            maxi = max(maxi, int(num))
        
        return maxi
