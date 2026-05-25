#User function Template for python3
class Solution:
	def removeVowels(self, s):
		# code here
		result = ""
		for ch in s:
		    if ch not in "aeiou":
		        result += ch
		return result 
