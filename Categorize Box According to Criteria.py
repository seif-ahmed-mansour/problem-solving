class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        if (length>=10**4 or width>=10**4 or height>=10**4 or (length*width*height)>=10**9) and mass>=100:
            return "Both"
        elif mass>=100:
            return "Heavy"
        elif length>=10**4 or width>=10**4 or height>=10**4 or (length*width*height)>=10**9:
            return "Bulky"
        else:
            return "Neither"
s=Solution()
print(s.categorizeBox(1000,35,700,300))