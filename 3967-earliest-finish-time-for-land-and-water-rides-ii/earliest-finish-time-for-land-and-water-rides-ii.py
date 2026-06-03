from typing import List
import bisect

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        def solve(firstStart, firstDur, secondStart, secondDur):
            # Sort second rides by start time
            rides = sorted(zip(secondStart, secondDur))

            starts = [s for s, d in rides]
            durs = [d for s, d in rides]

            n = len(rides)

            # prefixMinDur[i] = minimum duration from 0..i
            prefixMinDur = [0] * n
            prefixMinDur[0] = durs[0]

            for i in range(1, n):
                prefixMinDur[i] = min(prefixMinDur[i - 1], durs[i])

            # suffixMinFinish[i] = minimum (start + duration) from i..n-1
            suffixMinFinish = [0] * n
            suffixMinFinish[n - 1] = starts[n - 1] + durs[n - 1]

            for i in range(n - 2, -1, -1):
                suffixMinFinish[i] = min(
                    suffixMinFinish[i + 1],
                    starts[i] + durs[i]
                )

            ans = float('inf')

            # Try every ride from first category
            for s1, d1 in zip(firstStart, firstDur):
                finish1 = s1 + d1

                # first index where start > finish1
                idx = bisect.bisect_right(starts, finish1)

                # rides already open
                if idx > 0:
                    ans = min(ans, finish1 + prefixMinDur[idx - 1])

                # rides opening later
                if idx < n:
                    ans = min(ans, suffixMinFinish[idx])

            return ans

        # Try both orders
        return min(
            solve(landStartTime, landDuration,
                  waterStartTime, waterDuration),

            solve(waterStartTime, waterDuration,
                  landStartTime, landDuration)
        )