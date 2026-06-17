class Solution:
    def sortString(self, s: str) -> str:
        # code here
        arr = list(s) 
        arr.sort()
        
        return "".join(arr)
