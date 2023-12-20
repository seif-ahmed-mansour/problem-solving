class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for i in nums:
            while nums.count(i)>2:
                nums.remove(i)
        return len(nums)
s=Solution()
print(s.removeDuplicates([1,1,1,2,2,3]))