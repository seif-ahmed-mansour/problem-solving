class Solution:
    def countSeniors(self, details: list[str]) -> int:
        count=0
        for i in details:
            if int(str(i[-4])+str(i[-3]))>=60:
                count+=1
        return count
s=Solution()
print(s.countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))