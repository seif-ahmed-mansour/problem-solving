class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return i



s=Solution()
print(s.missingNumber([0,1]))
# fucking huge runtime idk why