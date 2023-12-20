class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        return all(nums[i] <= nums[i+1] for i in range(len(nums)-1)) or \
               all(nums[i] >= nums[i+1] for i in range(len(nums)-1))
s=Solution()
print(s.isMonotonic([1,2,2,3]))