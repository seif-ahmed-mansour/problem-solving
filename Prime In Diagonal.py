class Solution:
    def diagonalPrime(self, nums: list[list[int]]) -> int:
        prime=[]
        for i in nums:
            for j in i:
                def is_prime(num):
                    if num <= 1:
                        return False
                    for i in range(2, num):
                        if num % i == 0:
                            return False
                    return True
                if is_prime(j):
                    prime.append(j)
        return max(prime)
s=Solution()
print(s.diagonalPrime([[1,2,3],[5,6,7],[9,10,11]]))