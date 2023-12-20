class Solution:
    def majorityElement(self, nums: list[int]) -> int:
            return max(set(nums), key=nums.count)