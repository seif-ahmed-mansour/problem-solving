class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        count=0
        for i in words:
            if pref in i and pref[0:len(pref)]==i[0:len(pref)]:
                count+=1
        return count
s=Solution()
print(s.prefixCount(["pay","attention","practice","attend"],"at"))