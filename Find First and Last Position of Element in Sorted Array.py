class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        stack=[]
        for idx, i in enumerate(nums):
            if i == target:
                stack.append(idx)
                if idx == 0 and nums.count(i) == 1:
                    return [0, 0]
                if stack[-1] == nums.index(i) + nums.count(i) - 1:
                    return [stack[0], stack[-1]]
            if target not in nums:
                return [-1, -1]
        if not stack:
            return [-1, -1]
        else:
            return [stack[0], stack[-1]]

s = Solution()
print(s.searchRange([3, 3, 3], 3))