from functools import cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(n: int) -> int:
            if n < 0:
                return 0

            s = str(n)
            m = len(s)

            @cache
            def dp(pos, tight, started, length, last1, last2):
                if pos == m:
                    return (1, 0)  # (count, waviness_sum)

                limit = int(s[pos]) if tight else 9

                total_count = 0
                total_wavy = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            False,
                            0,
                            10,
                            10
                        )
                        total_count += cnt
                        total_wavy += wav
                        continue

                    if not started:
                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            True,
                            1,
                            d,
                            10
                        )
                        total_count += cnt
                        total_wavy += wav
                        continue

                    add = 0

                    if length >= 2:
                        if (last1 > last2 and last1 > d) or (
                            last1 < last2 and last1 < d
                        ):
                            add = 1

                    cnt, wav = dp(
                        pos + 1,
                        ntight,
                        True,
                        length + 1,
                        d,
                        last1
                    )

                    total_count += cnt
                    total_wavy += wav + add * cnt

                return (total_count, total_wavy)

            return dp(0, True, False, 0, 10, 10)[1]

        return solve(num2) - solve(num1 - 1)