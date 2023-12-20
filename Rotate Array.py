class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        if k==0:return 1
        a=nums[:len(nums)-k]
        b=nums[len(nums)-k:];
        c=b+a
        for num in range(0,len(nums)):
            nums[num]=c[num]
s=Solution()
print(s.rotate([1,2],3))