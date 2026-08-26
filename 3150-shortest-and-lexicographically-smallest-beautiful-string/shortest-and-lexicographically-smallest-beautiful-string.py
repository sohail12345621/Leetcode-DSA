class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = [i for i, ch in enumerate(s) if ch == '1']

        if len(ones) < k:
            return ""

        min_len = float('inf')
        ans = ""

        for i in range(len(ones) - k + 1):
            left = ones[i]
            right = ones[i + k - 1]

            candidate = s[left:right + 1]
            length = len(candidate)

            if length < min_len:
                min_len = length
                ans = candidate
            elif length == min_len and candidate < ans:
                ans = candidate

        return ans