class Solution:
    def convert(self, s: str) -> str:
        # code here

        result = ""

        for i in range(len(s)):

            if i == 0 or s[i - 1] == ' ':
                result += s[i].upper()
            else:
                result += s[i]

        return result        
                
