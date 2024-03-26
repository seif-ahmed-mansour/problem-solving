
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        for i in range(1, len(nums)+2):
            if i not in nums_set:
                return i
s = Solution()
print(s.firstMissingPositive([3, 4, -1, 1]))
