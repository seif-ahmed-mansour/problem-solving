class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        lolo=[]
        for i in nums1:
            if i in nums2:
                lolo.append(i)
            elif len(nums2)==1 :
                return [lolo[0]]
        return lolo
s=Solution()
print(s.intersect([1],[1]))