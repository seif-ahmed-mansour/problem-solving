class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in s:
            if s.count(i) == 1:
                return s.index(i)
        return -1
s=Solution()
print(s.firstUniqChar("loveleetcode"))