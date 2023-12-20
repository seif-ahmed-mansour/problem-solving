class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        x=sorted(nums)
        lolooo=[]
        for i,el in enumerate(x):
            if el ==target:
                lolooo.append(i)
        return lolooo
s=Solution()
print(s.targetIndices([1,2,5,2,3],2))