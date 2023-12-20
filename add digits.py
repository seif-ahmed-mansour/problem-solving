class Solution:
    def addDigits(self, num: int) -> int:
        x = str(num)
        y = [int(digit) for digit in x]
        while len(y) > 1:
            z = sum(y)
            x = str(z)
            y = [int(digit) for digit in x]
        return y[0]

s = Solution()
print(s.addDigits(12))