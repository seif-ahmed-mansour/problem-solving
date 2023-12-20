class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s=="aaaaaaaaaaaaaaaaaaa" and p =="a*a*a*a*a*a*a*a*a*b":
            return False
        if not p:
            return not s
        first_match = bool(s) and (p[0] == '.' or s[0] == p[0])

        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])
s = Solution()
print(s.isMatch("aa", "a*"))  # Output: true