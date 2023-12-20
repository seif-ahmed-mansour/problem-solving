class Solution:
    def reverse(self, x: int) -> int:
        stringX = str(abs(x))
        revString = stringX[::-1]
        output = int(revString)
        if(output > 2147483647):
            return 0
        return output if x > 0 else (-1)*output

s = Solution()
print(s.reverse(-123))