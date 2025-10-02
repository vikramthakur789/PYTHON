#Back-end complete function Template for Python 3


class Solution:
    # Function to find a continuous sub-array which adds up to a given number
    def subarraySum(self, arr, target):
        s = 0
        curr = 0

        for e in range(len(arr)):
            curr += arr[e]

            # Adjust the start of the window if the current sum exceeds the target
            while curr > target and s < e:
                curr -= arr[s]
                s += 1

            # If the current sum equals the target, return the 1-based indices
            if curr == target:
                return [s + 1, e + 1]

        # If no subarray is found
        return [-1]
