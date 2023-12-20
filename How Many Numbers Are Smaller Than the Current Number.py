class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        fss = sorted(nums)
        lolo = {}
        result = []
        for i in range(len(fss)):
            if fss[i] not in lolo:
                lolo[fss[i]] = i
        for i in range(len(nums)):
            result.append(lolo[nums[i]])
        return result
