class Solution:
    def firstRep(self, s):
        freq = {}
        
        # count frequency
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        # find first repeating
        for ch in s:
            if freq[ch] > 1:
                return ch
        
        return -1
