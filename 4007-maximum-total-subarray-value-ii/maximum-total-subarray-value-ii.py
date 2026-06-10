from typing import List
import heapq

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Sparse Tables
        LOG = (n).bit_length()

        st_max = [nums[:]]
        st_min = [nums[:]]

        j = 1
        while (1 << j) <= n:
            length = 1 << j
            half = length >> 1

            mx = [0] * (n - length + 1)
            mn = [0] * (n - length + 1)

            for i in range(n - length + 1):
                mx[i] = max(st_max[j - 1][i],
                            st_max[j - 1][i + half])
                mn[i] = min(st_min[j - 1][i],
                            st_min[j - 1][i + half])

            st_max.append(mx)
            st_min.append(mn)
            j += 1

        log = [0] * (n + 1)
        for i in range(2, n + 1):
            log[i] = log[i // 2] + 1

        def value(l: int, r: int) -> int:
            length = r - l + 1
            p = log[length]

            mx = max(
                st_max[p][l],
                st_max[p][r - (1 << p) + 1]
            )

            mn = min(
                st_min[p][l],
                st_min[p][r - (1 << p) + 1]
            )

            return mx - mn

        # Max Heap
        pq = []

        for l in range(n):
            r = n - 1
            v = value(l, r)
            heapq.heappush(pq, (-v, l, r))

        ans = 0

        for _ in range(k):
            neg_v, l, r = heapq.heappop(pq)
            ans += -neg_v

            if r > l:
                nr = r - 1
                nv = value(l, nr)
                heapq.heappush(pq, (-nv, l, nr))

        return ans