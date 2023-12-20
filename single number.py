# class Solution:
#     def singleNumber(self, nums: list[int]) -> int:
#         stack=[]
#         for i in nums:
#             if i in stack:
#                 stack.remove(i)
#             else:
#                 stack.append(i)
#         return stack.pop()
#
# s=Solution()
# print(s.singleNumber([2,2,1]))
class Solution(object):
    def singleNumber(self, nums: list[int]) -> int:
        lolo=set()
        for i in nums:
            if i not in lolo:
                lolo.add(i)
            else:
                lolo.remove(i)
        for x in lolo:
            return x

s=Solution()
print(s.singleNumber([2,2,1]))