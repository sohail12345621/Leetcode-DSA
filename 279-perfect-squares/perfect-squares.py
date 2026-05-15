class Solution:
    def numSquares(self, n: int) -> int:

        # dp[i] = minimum squares needed for i
        dp = [float('inf')] * (n + 1)

        # Base case
        dp[0] = 0

        # Fill dp array
        for i in range(1, n + 1):

            j = 1

            # Try every perfect square <= i
            while j * j <= i:

                square = j * j

                dp[i] = min(
                    dp[i],
                    1 + dp[i - square]
                )

                j += 1

        return dp[n]