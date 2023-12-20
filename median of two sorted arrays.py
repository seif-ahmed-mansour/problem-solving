class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged=sorted(nums1+nums2)
        n=len(merged)
        lolo = n // 2
        if n%2==0:
            return ((merged[lolo]+merged[lolo-1])/2)
        else:
            return merged[lolo]
s=Solution()
print(s.findMedianSortedArrays([1,2],[3,4]))
