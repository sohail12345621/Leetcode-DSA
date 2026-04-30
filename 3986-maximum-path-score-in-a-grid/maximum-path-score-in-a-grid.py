class Solution:
    def maxPathScore(self, grid, k):
        m, n = len(grid), len(grid[0])
        
        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 0
        
        for i in range(m):
            for j in range(n):
                for c in range(k + 1):
                    if dp[i][j][c] == -1:
                        continue
                    
                    # Right
                    if j + 1 < n:
                        val = grid[i][j + 1]
                        cost = 0 if val == 0 else 1
                        new_cost = c + cost
                        
                        if new_cost <= k:
                            dp[i][j + 1][new_cost] = max(
                                dp[i][j + 1][new_cost],
                                dp[i][j][c] + val
                            )
                    
                    # Down
                    if i + 1 < m:
                        val = grid[i + 1][j]
                        cost = 0 if val == 0 else 1
                        new_cost = c + cost
                        
                        if new_cost <= k:
                            dp[i + 1][j][new_cost] = max(
                                dp[i + 1][j][new_cost],
                                dp[i][j][c] + val
                            )
        
        res = max(dp[m - 1][n - 1])
        return res if res != -1 else -1