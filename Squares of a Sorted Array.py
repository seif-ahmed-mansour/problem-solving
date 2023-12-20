class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        lolooo=[]
        for i in nums:
            lolooo.append(i**2)
        return sorted(lolooo)
s=Solution()
print(s.sortedSquares([-4,-1,0,3,10]))