
class Solution:
    def rotate(self, arr):
        last = arr[-1]          # store last element
        
        for i in range(len(arr)-1, 0, -1):
            arr[i] = arr[i-1]   # shift elements right
        
        arr[0] = last           # put last element at first
        return arr
    
