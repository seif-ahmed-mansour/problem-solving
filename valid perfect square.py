class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        from math import sqrt,floor
        return sqrt(num) == floor(sqrt(num))
s = Solution()
print(s.isPerfectSquare(1))
