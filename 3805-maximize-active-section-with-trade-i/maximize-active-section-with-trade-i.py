class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = "1" + s + "1"
        runs = []

        i = 0
        while i < len(t):
            j = i
            while j < len(t) and t[j] == t[i]:
                j += 1
            runs.append((t[i], j - i))
            i = j

        active = s.count("1")

        top1 = (-1, -1)
        top2 = (-1, -1)

        for idx, (ch, length) in enumerate(runs):
            if ch == "0":
                if length > top1[0]:
                    top2 = top1
                    top1 = (length, idx)
                elif length > top2[0]:
                    top2 = (length, idx)

        ans = active

        for i in range(1, len(runs) - 1):
            if runs[i][0] != "1":
                continue

            one_len = runs[i][1]
            left_zero = runs[i - 1][1]
            right_zero = runs[i + 1][1]

            ans = max(ans, active + left_zero + right_zero)

            if top1[1] != i - 1 and top1[1] != i + 1:
                best_other = top1[0]
            else:
                best_other = top2[0] if top2[1] != -1 else 0

            ans = max(ans, active - one_len + best_other)

        return ans