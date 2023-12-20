class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for idx, i in enumerate(nums):
            if i == target:
                return idx
            elif i > target:
                return idx
        return len(nums)

s = Solution()
print(s.searchInsert([1,3,5,6], 7))
