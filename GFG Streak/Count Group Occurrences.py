class Solution:
    def getCount (self, s, k):
        # code here

        mp = {}
        i = 0
        n = len(s)

        while i < n:
            ch = s[i]
            mp[ch] = mp.get(ch, 0) + 1

            while i < n - 1 and s[i] == s[i + 1]:
                i += 1

            i += 1

        ans = 0

        for value in mp.values():
            if value == k:
                ans += 1

        return ans
