class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        total=0
        stack=[]
        for i in nums:
            if i ==1:
                total+=1
            elif i==0:
                stack.append(total)
                total=0
        stack.append(total)
        return max(stack)
s=Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))