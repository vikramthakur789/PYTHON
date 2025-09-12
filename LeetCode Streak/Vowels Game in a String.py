class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = set('aeiou')
        
        # Check if the string contains at least one vowel
        for c in s:
            if c in vowels:
                return True  # Alice can make a move and will always win
        
        # If there are no vowels, Alice has no valid move and loses
        return False
