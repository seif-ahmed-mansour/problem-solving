# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         for i in nums:
#             if nums.count(i)>1:
#                 return True
#         return False
# s=Solution()
# print(s.containsDuplicate([1,2,3,4]))

# the last way takes alot of time bec of its time complexty and it gives timie limit exeeded in leet code
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # hya mesh stach bs ana krrt asameha stack
        stack=set()
        for i in nums:
            if i in stack:
                return True
            else:
                stack.add(i)
s=Solution()
print(s.containsDuplicate([1,2,3,1]))
