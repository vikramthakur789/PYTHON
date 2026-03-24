class Solution:
    def reverseWords(self, s):
        # code here
                return ".".join([word for word in s.split('.') if word][::-1])
