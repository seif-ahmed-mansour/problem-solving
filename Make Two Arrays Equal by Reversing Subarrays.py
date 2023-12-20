class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        if len(target) != len(arr):
            return False
        target.sort()
        arr.sort()
        return target == arr
s=Solution()
print(s.canBeEqual([1,2,3,4],[2,4,1,3]))