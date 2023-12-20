class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n=len(nums)//3
        appear=set()
        for i in nums:
            if nums.count(i) > n:
                appear.add(i)
        return list(appear)
s=Solution()
print(s.majorityElement([3,2,3]))

