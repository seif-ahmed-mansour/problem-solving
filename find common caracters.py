class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        common = []

        for char in words[0]:
            if all(char in word for word in words[1:]):
                common.append(char)
                words = [word.replace(char, '', 1) for word in words]

        return common



