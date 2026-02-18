class Solution:
    def largest(self, arr):
        # code here
        max_arr = -10000000;
        for num in arr:
            if num > max_arr:
                max_arr = num
        return max_arr
  
