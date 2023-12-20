class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        lolo=set()
        for i in nums:
            if i not in lolo:
                lolo.add(i)
            else:
                lolo.remove(i)
        for x in lolo:
            return x

s=Solution()
print(s.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
