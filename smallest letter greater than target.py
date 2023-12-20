class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        stack=[]
        for i in letters:
            if i>target:
                stack.append(i)
                return min(stack)
        return letters[0]
s=Solution()
print(s.nextGreatestLetter(["c","f","j"],"c"))
