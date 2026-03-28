class Solution:
    def minPartitions(self, n: str) -> int:
        max_digit = 0
        for ch in n:
            digit = int(ch)
            if digit > max_digit:
                max_digit = digit
                if max_digit == 9:
                    return 9
        return max_digit