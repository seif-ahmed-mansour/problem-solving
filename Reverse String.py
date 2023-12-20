class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return s[::-1]
    # it worked on leetcode by reverse func but here no and vise versa
s=Solution()
print(s.reverseString(["h","e","l","l","o"]))