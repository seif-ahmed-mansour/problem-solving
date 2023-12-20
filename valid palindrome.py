class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                left_removed = s[l+1:r+1]
                right_removed = s[l:r]
                if left_removed == left_removed[::-1] or right_removed == right_removed[::-1]:
                    return True
                else:
                    return False
            l += 1
            r -= 1
        return True


s=Solution()
print(s.validPalindrome("abca"))