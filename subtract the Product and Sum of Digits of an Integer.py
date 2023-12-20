class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        from math import prod
        x = str(n)
        y = [int(digit) for digit in x]

        product=prod(y)
        lolo=sum(y)
        result=product - lolo
        return result
s=Solution()
print(s.subtractProductAndSum(234))