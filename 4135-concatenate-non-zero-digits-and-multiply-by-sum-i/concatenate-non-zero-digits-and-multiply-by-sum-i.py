class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        digit_sum = 0

        for ch in str(n):
            digit = int(ch)

            if digit != 0:
                x = x * 10 + digit
                digit_sum += digit

        return x * digit_sum