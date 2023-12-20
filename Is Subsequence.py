class Solution(object):
    def isSubsequence(self, s, t):
        if not s:
            return True
        i = 0
        for j in t:
            if j == s[i]:
                i += 1
            if i == len(s):
                break
        return i == len(s)
s=Solution()
print(s.isSubsequence("abc","ahbgdc"))
# print(s.isSubsequence())