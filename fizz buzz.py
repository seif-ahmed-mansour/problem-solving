class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        lolo=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                lolo.append("FizzBuzz")
            elif i%3==0:
                lolo.append("Fizz")
            elif i%5==0:
                lolo.append("Buzz")
            else:
                lolo.append(str(i))
        return lolo
s=Solution()
print(s.fizzBuzz(5))