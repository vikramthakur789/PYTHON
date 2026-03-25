class Solution:
    # Function to find uncommon characters between two strings.
    def uncommonChars(self, s1, s2):
        #code here
         return "".join(sorted((set(s1) ^ set(s2))))
