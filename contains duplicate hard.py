class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff <= 0 or valueDiff < 0:
            return False
        buckets = {}
        for i in range(len(nums)):
            bucket_index = nums[i] // (valueDiff + 1)
            if bucket_index in buckets:
                return True
            if bucket_index - 1 in buckets and abs(nums[i] - buckets[bucket_index - 1]) <= valueDiff:
                return True
            if bucket_index + 1 in buckets and abs(nums[i] - buckets[bucket_index + 1]) <= valueDiff:
                return True
            buckets[bucket_index] = nums[i]
            if i >= indexDiff:
                left_bucket_index = nums[i - indexDiff] // (valueDiff + 1)
                del buckets[left_bucket_index]
s=Solution()
print(s.containsNearbyAlmostDuplicate([1,2,3,1],3,0))