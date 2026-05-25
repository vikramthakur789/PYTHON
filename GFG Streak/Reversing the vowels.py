#User function Template for python3

class Solution:
    def modify(self, s):
        # code here
        arr = list(s)
        left = 0
        
        right = len(arr) - 1
        
        vowels = "aeiou"
        
        while left < right:
            while left < right and arr[left] not in vowels:
                left += 1
                
            while left < right and arr[right] not in vowels:
                right -= 1
                
            arr[left], arr[right] = arr[right], arr[left]
            
            left += 1
            right -= 1
            
        return"".join(arr)    
