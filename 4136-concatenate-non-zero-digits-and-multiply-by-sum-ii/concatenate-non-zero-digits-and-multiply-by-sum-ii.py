from typing import List
import bisect

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7

        positions = []
        digits = []

        for i, ch in enumerate(s):
            if ch != '0':
                positions.append(i)
                digits.append(int(ch))

        k = len(digits)

        pow10 = [1] * (k + 1)
        for i in range(1, k + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        pref_num = [0] * (k + 1)
        pref_sum = [0] * (k + 1)

        for i in range(k):
            pref_num[i + 1] = (pref_num[i] * 10 + digits[i]) % MOD
            pref_sum[i + 1] = pref_sum[i] + digits[i]

        ans = []

        for l, r in queries:
            left = bisect.bisect_left(positions, l)
            right = bisect.bisect_right(positions, r) - 1

            if left > right:
                ans.append(0)
                continue

            length = right - left + 1

            x = (pref_num[right + 1] - pref_num[left] * pow10[length]) % MOD
            digit_sum = pref_sum[right + 1] - pref_sum[left]

            ans.append((x * digit_sum) % MOD)

        return ans