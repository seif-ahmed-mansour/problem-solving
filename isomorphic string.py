class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for i in range(len(s)):
            if s[i] not in s_map and t[i] not in t_map:
                s_map[s[i]] = t[i]
                t_map[t[i]] = s[i]
            elif s[i] in s_map and t[i] in t_map:
                if s_map[s[i]] != t[i] or t_map[t[i]] != s[i]:
                    return False
            else:
                return False

        return True
s=Solution()
print(s.isIsomorphic("egg","add"))