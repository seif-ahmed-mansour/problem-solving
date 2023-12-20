class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        answers=[]
        return answers+[celsius + 273.15]+[celsius * 1.80 + 32.00]
s=Solution()
print(s.convertTemperature(36.50))