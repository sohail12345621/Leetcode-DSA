class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(t)

        # dp[j] = number of ways to form t[:j] from characters processed in s
        dp = [0] * (m + 1)
        dp[0] = 1

        for ch in s:
            # Traverse backwards so each character of s is used only once
            for j in range(m, 0, -1):
                if ch == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[m]