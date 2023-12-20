class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        s = str(num)
        s1 = int(s[::-1])
        s2 = str(s1)
        print(s2[::-1])
        return int(s2[::-1])==int(s)

s=Solution()
print(s.isSameAfterReversals(526))