from collections import Counter
from math import lgamma, exp

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)

        half = [0] * 26
        mid = ""
        m = 0
        for i in range(26):
            c = cnt.get(chr(i + 97), 0)
            half[i] = c // 2
            m += half[i]
            if c % 2:
                mid = chr(i + 97)

        LIMIT = 10 ** 6

        # Count distinct permutations of the remaining half (capped at LIMIT)
        def ways(arr):
            total = sum(arr)

            # Fast logarithmic estimate
            logv = lgamma(total + 1)
            for x in arr:
                logv -= lgamma(x + 1)

            if logv > 14.0:      # e^14 > 1e6
                return LIMIT

            val = round(exp(logv))
            if val > LIMIT:
                return LIMIT
            return val

        if ways(half) < k:
            return ""

        first = []

        for _ in range(m):
            for c in range(26):
                if half[c] == 0:
                    continue

                half[c] -= 1
                w = ways(half)

                if k > w:
                    k -= w
                    half[c] += 1
                else:
                    first.append(chr(c + 97))
                    break

        left = "".join(first)
        return left + mid + left[::-1]