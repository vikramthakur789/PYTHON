class Solution:
    def binarySubstring(self, s):
        MOD = 1000000007
        
        count = 0
        for ch in s:
            if ch == '1':
                count += 1
        
        return (count * (count - 1) // 2) % MOD
