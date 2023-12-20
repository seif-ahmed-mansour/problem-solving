class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:
        dp = {}
        dp[0] = 0

        for rod in rods:
            curr_dp = dp.copy()
            for diff, height in curr_dp.items():
                if diff + rod not in dp:
                    dp[diff + rod] = height
                else:
                    dp[diff + rod] = max(dp[diff + rod], height)
                if abs(diff - rod) not in dp:
                    dp[abs(diff - rod)] = height + min(diff, rod)
                else:
                    dp[abs(diff - rod)] = max(dp[abs(diff - rod)], height + min(diff, rod))

        return dp[0]
s=Solution()
print(s.tallestBillboard([1,2,3,6]))