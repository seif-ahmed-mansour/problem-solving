class Solution:
    def canSeePersonsCount(self, A):
        n = len(A)
        stack, res = [], [0] * n
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= A[i]:
                stack.pop()
                res[i] += 1
            if stack: res[i] += 1
            stack.append(A[i])
        return res
s=Solution()
print(s.canSeePersonsCount([10,6,8,5,11,9]))