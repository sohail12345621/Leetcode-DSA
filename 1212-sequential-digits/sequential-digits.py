class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        ans = []

        for start in range(1, 10):
            num = start
            next_digit = start + 1

            while next_digit <= 9:
                num = num * 10 + next_digit

                if low <= num <= high:
                    ans.append(num)

                next_digit += 1

        ans.sort()
        return ans