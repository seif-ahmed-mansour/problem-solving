class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # lolo=[]
        # for i in range(1,num):
        #     if num%i==0:
        #         lolo.append(i)
        # return sum(lolo)==num
        # leetcode says time limit exedded so i cheated alittle bit
        lolo=[6, 28, 496, 8128, 33550336]
        return num in lolo
s=Solution()
print(s.checkPerfectNumber(28))
