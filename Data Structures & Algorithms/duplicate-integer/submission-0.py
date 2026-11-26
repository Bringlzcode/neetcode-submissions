class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
     nums.sort()
     dupe = False
     for i in range(len(nums)-1):
      if nums[i] == nums[i+1]:
        dupe = True
     return dupe
       
