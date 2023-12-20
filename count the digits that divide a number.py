class Solution:
    def countDigits(self, num: int) -> int:
        x=str(num)
        count=0
        for i in x:
            if num%int(i)==0:
                count+=1
        return count
s=Solution()
print(s.countDigits(121))
