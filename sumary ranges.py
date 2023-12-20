class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        res = []
        start = end = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                res.append(str(start) + '->' + str(end) if start != end else str(start))
                start = end = nums[i]
        res.append(str(start) + '->' + str(end) if start != end else str(start))
        return res
s=Solution()
print(s.summaryRanges([0,1,2,4,5,7]))