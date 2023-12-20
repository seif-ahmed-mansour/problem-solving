class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = []
        count = 0
        max_count = 0
        for i in s:
            if i not in stack:
                stack.append(i)
                count += 1
            else:
                max_count = max(max_count, count)
                while stack[0] != i:
                    stack.pop(0)
                    count -= 1
                stack.pop(0)
                stack.append(i)
        max_count = max(max_count, count)
        return max_count