class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = 1
        result = 0
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c == '+':
                result += sign*num
                num = 0
                sign = 1
            elif c == '-':
                result += sign*num
                num = 0
                sign = -1
            elif c == '(':
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif c == ')':
                result += sign*num
                num = 0
                result *= stack.pop()
                result += stack.pop()
        return result + sign*num
s=Solution()
print(s.calculate("1 + 1"))