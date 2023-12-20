class Solution:
    def countElements(self, nums: list[int]) -> int:
        count=0
        for i in nums:
            if i !=max(nums) and i !=min(nums):
                count+=1
        return count
s=Solution()
print(s.countElements([11,7,2,15]))