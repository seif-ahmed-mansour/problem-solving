class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        if s[0]==s[-1] and x>=0:
            return "true"
        else:
            return "false"
s=Solution()
print(s.isPalindrome(1234231))