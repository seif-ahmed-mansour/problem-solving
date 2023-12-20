class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""


s=Solution()
print(s.firstPalindrome(["abc","car","ada","racecar","cool"]))