class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        matrix[:] = zip(*matrix[::-1])
        # return matrix
s=Solution()
print(s.rotate([[1,2,3],[4,5,6],[7,8,9]]))