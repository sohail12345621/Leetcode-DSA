from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # Store: (left, right, weight, original_index)
        arr = [
            (l, r, w, i)
            for i, (l, r, w) in enumerate(intervals)
        ]

        # Sort by right endpoint
        arr.sort(key=lambda x: x[1])

        # Right endpoints for binary search
        rights = [x[1] for x in arr]

        # prev[i] = number of intervals before i that can be
        # used together with interval i
        #
        # We need right < current_left, NOT <=
        prev = []
        for i in range(n):
            left = arr[i][0]
            j = bisect_left(rights, left)
            prev.append(j)

        # dp[k][i] = best (score, indices) using at most k intervals
        # from arr[0:i]
        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        def better(a, b):
            """
            Return the better of two states.
            Higher score wins.
            If scores are equal, lexicographically smaller
            index tuple wins.
            """
            if a[0] != b[0]:
                return a if a[0] > b[0] else b

            return a if a[1] < b[1] else b

        for k in range(1, 5):
            for i in range(1, n + 1):
                # Don't take current interval
                best = dp[k][i - 1]

                # Take current interval
                left, right, weight, original_idx = arr[i - 1]

                p = prev[i - 1]

                previous_score, previous_indices = dp[k - 1][p]

                candidate = (
                    previous_score + weight,
                    tuple(sorted(previous_indices + (original_idx,)))
                )

                best = better(best, candidate)

                dp[k][i] = best

        return list(dp[4][n][1])