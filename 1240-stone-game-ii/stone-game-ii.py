class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = total stones from i to end
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        # dp(i, M) = maximum stones current player can get
        # starting from index i with current M
        from functools import lru_cache

        @lru_cache(None)
        def dp(i, M):
            if i >= n:
                return 0

            # Can take all remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            best = 0

            # Try taking X piles, where 1 <= X <= 2M
            for X in range(1, 2 * M + 1):
                # Stones current player gets
                taken = suffix[i] - suffix[i + X]

                # Opponent gets the best they can from remaining piles
                opponent = dp(i + X, max(M, X))

                # Total remaining stones - opponent's best
                current = suffix[i] - opponent

                best = max(best, current)

            return best

        return dp(0, 1)