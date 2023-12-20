class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) ->list[int]:
        lolo=set()
        for i in nums1:
            if i in nums2:
                lolo.add(i)
        return lolo
s=Solution()
print(s.intersection([4,9,5],[9,4,9,8,4]))