class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min=nums[0]
        for i in nums:
            if i <min:
                min=i
        return min
s=Solution()
print(s.findMin([10,3,5]))
##############################
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i in nums:
#             if nums[i]+nums[i+1]==target:
#                 return [i,i+1]
# x=Solution()
# print(x.twoSum([2,7,11,15],9))