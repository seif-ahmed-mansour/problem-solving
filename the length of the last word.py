class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x=s.split()
        s=x[-1]
        print(len(s))
s=Solution()
s.lengthOfLastWord("Hello World")