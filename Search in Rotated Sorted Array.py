class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if target not in nums:
            return -1
        return nums.index(target)
s=Solution()
print(s.search([4,5,6,7,0,1,2],0))