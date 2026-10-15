class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        right = 0
        sumofCurrentWindow = 0
        res = float('inf')

        for right in range(0, len(nums)):
            sumofCurrentWindow += nums[right]

            while sumofCurrentWindow >= target:
                res = min(res, right - left + 1)
                sumofCurrentWindow -= nums[left]
                left += 1

        return res if res != float('inf') else 0