class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        lolo=[]
        for i in nums:
            if i not in lolo:
                lolo.append(i)
            else:
                lolo.remove(i)
        return lolo[0:2]
s=Solution()
print(s.singleNumber([1,2,1,3,2,5]))