class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_val = 0
        for i in nums:
            if i == 1:
                counter += 1
            else:
                counter = 0
            if counter > max_val:
                max_val = counter
        return max_val
        