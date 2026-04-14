class Solution:
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()

        n = len(robot)
        m = len(factory)

        # Initialize DP
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        # Fill DP
        for j in range(1, m + 1):
            pos, cap = factory[j - 1]

            for i in range(0, n + 1):
                # Case 1: skip this factory
                dp[i][j] = dp[i][j - 1]

                # Case 2: assign k robots to this factory
                dist = 0
                for k in range(1, min(cap, i) + 1):
                    dist += abs(robot[i - k] - pos)
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i - k][j - 1] + dist
                    )

        return dp[n][m]