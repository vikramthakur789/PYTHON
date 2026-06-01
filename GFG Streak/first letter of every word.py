#User function Template for python3
class Solution:
	def firstAlphabet(self, s):
		# code here
		result = s[0]
		for i in range(len(s)):
		    if s[i] == " ":
		        result += s[i + 1]
		        
		        
		return result        
		        
