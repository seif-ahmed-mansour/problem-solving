class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack=[]
        for op in operations:
            if op=="+":
                if len(stack)>=2:
                    stack.append(stack[-1]+stack[-2])
            elif op=="D":
                if len(stack)>=1:
                    stack.append(stack[-1]*2)
            elif op=="C":
                if len(stack)>=1:
                    stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)
s=Solution()
print(s.calPoints(["5","2","C","D","+"]))