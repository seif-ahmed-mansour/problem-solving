class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        count=0
        for i in grid:
            for j in i:
              if j<=0:
                count+=1
        return count
s=Solution()
print(s.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))