class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)

        # If total is odd, impossible
        if total % 2 != 0:
            return False

        target = total // 2

        # dp[s] = can we make sum s?
        dp = [False] * (target + 1)

        dp[0] = True

        for num in nums:

            # Traverse backwards
            for s in range(target, num - 1, -1):

                dp[s] = dp[s] or dp[s - num]

        return dp[target]