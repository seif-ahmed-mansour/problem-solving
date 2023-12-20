class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        x=sorted(nums)
        return x[-k]
s=Solution()
print(s.findKthLargest([3,2,1,5,6,4],2))