class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for i in items:
            if ruleKey == "type":
                if ruleValue == i[0]:
                    count += 1
            elif ruleKey == "color":
                if ruleValue == i[1]:
                    count += 1
            elif ruleKey == "name":
                if ruleValue == i[2]:
                    count += 1
        return count