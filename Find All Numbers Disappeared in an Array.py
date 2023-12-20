class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        lolo = set()
        for i, num in enumerate(nums):
            lolo.add(num)
        disappeared = []
        for i in range(1, len(nums) + 1):
            if i not in lolo:
                disappeared.append(i)
        return disappeared

s=Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
