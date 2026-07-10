from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Sort nodes by value
        order = sorted((nums[i], i) for i in range(n))
        values = [x[0] for x in order]

        pos = [0] * n
        for i, (_, idx) in enumerate(order):
            pos[idx] = i

        comp = [0] * n
        cid = 0
        for i in range(1, n):
            if values[i] - values[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid

        nextReach = [0] * n
        r = 0
        for l in range(n):
            while r + 1 < n and values[r + 1] - values[l] <= maxDiff:
                r += 1
            nextReach[l] = r

        LOG = n.bit_length()

        up = [nextReach]
        for _ in range(1, LOG):
            prev = up[-1]
            cur = [0] * n
            for i in range(n):
                cur[i] = prev[prev[i]]
            up.append(cur)

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            pu = pos[u]
            pv = pos[v]

            if pu > pv:
                pu, pv = pv, pu

            if comp[pu] != comp[pv]:
                ans.append(-1)
                continue

            cur = pu
            steps = 0

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < pv:
                    cur = up[k][cur]
                    steps += 1 << k

            ans.append(steps + 1)

        return ans