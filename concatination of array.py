class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans=nums+nums
        return ans
s=Solution()
print(s.getConcatenation([1,2,1]))