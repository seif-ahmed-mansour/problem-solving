class Solution:
    def findMin(self, nums: list[int]) -> int:
        min = nums[0]
        for i in nums:
            if i < min:
                min = i
        return min