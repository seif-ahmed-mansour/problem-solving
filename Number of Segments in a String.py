class Solution:
    def countSegments(self, s: str) -> int:
        x=s.split(" ")
        count=0
        for i in x:
            if i !=" " and i!="":
                count+=1
        return count
s=Solution()
print(s.countSegments("Hello, my name is John"))