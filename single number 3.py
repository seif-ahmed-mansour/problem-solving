class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        lolo=[]
        for i in nums:
            if i not in lolo:
                lolo.append(i)
            else:
                lolo.pop()
        for x in lolo:
            return x
s=Solution()
print(s.singleNumber([2,2,3,2]))
