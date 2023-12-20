class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        non_dups=set()
        dups=[]
        for i in nums:
            if i not in non_dups:
                non_dups.add(i)
            else:
                dups.append(i)
        return dups
s=Solution()
print(s.findDuplicates([4,3,2,7,8,2,3,1]))