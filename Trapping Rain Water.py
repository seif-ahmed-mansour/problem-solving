class Solution:
    def trap(self, height: list[int]) -> int:
        stack = []
        trapped_rainwater = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top_of_stack = stack.pop()
                if stack:
                    trapped_rainwater += (min(height[i], height[stack[-1]]) - height[top_of_stack]) * (
                                i - stack[-1] - 1)
            stack.append(i)
        while stack:
            top_of_stack = stack.pop()
            if stack:
                trapped_rainwater += (min(height[stack[-1]], height[top_of_stack]) - height[top_of_stack]) * (
                            len(height) - stack[-1] - 1)
        return trapped_rainwater
s=Solution()
print(s.trap([4,2,0,3,2,5]))