class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        # lolo=[]
        # for i in nums:
        #     if i not in lolo:
        #         lolo.append(i)
        #     else:
        #         lolo.remove(i)
        # return sum(lolo)
        lolo=[]
        for i in nums:
            if nums.count(i)==1:
                lolo.append(i)
        return sum(lolo)
s=Solution()
print(s.sumOfUnique([1,2,3,2]))