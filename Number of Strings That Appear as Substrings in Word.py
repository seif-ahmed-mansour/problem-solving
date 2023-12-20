class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        count=0
        for i in patterns:
            if i in word:
                count+=1
        return count
s=Solution()
print(s.numOfStrings(["a","abc","bc","d"],"abc"))