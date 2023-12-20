class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        count = [0] * (n + 1)
        for num in nums:
            count[num] += 1

        duplicate = -1
        missing = -1
        for i in range(1, len(count)):
            if count[i] == 2:
                duplicate = i
            elif count[i] == 0:
                missing = i

        return [duplicate, missing]

s = Solution()
print(s.findErrorNums([1, 1]))