class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = sorted(s)
        t_chars = sorted(t)
        return s_chars == t_chars

s = Solution()
print(s.isAnagram("anagram", "nagaram"))