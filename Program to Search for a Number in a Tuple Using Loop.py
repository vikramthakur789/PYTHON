nums = (1,4,9,81,16,25,81,36,49,64,81,100)
x = 81
i = 0 #initialization
while i < len(nums):
   if (nums[i] == x):   
      print("found at idx", i)
   else:
      print("finding..")   

   i += 1
   
