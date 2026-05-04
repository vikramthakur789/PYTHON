class Solution:
    def remAnagram(self, s1, s2):
        # code here
        freq = [0] * 26
        
        # count s1
        for ch in s1:
            freq [ord(ch)  - ord("a")] +=1
            
        # count s2
        for ch in s2:
            freq [ord(ch) - ord("a")] -=1
            
            
        # sum absolute diffrences
        count = 0
        for x in freq:
            count += abs(x)
            
        return count    
        
