class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        unique_values = set(nums)
        nums = list(unique_values)
        nums.sort()
        if len(nums) < 3:
            return max(nums)
        elif len(nums) == 3:
            return min(nums)
        else:
            return nums[-3]
s = Solution()
print(s.thirdMax([1, 2]))
