class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # lolo=[]
        # for i in nums:
        #     if i not in lolo:
        #         lolo.append(i)
        #     else:
        #         return i
        # from collections import Counter
        # counter=Counter(nums)
        # return counter.most_common(1)[0][0]
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

s=Solution()
print(s.findDuplicate([1,3,4,2,2]))