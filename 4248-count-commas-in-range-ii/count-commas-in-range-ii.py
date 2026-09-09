class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        power = 1000
        commas = 1

        while power <= n:
            # Numbers from power to n have at least
            # this comma position.
            ans += n - power + 1

            power *= 1000
            commas += 1

        return ans