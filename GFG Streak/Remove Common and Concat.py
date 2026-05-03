class Solution:
    def concatenatedString(self, s1, s2):
        result = ""
        
        # from s1
        for ch in s1:
            if ch not in s2:
                result += ch
        
        # from s2
        for ch in s2:
            if ch not in s1:
                result += ch
        
        if result == "":
            return "-1"
        
        return result
