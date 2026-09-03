class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        min_odd = float('inf')

        # Find the smallest odd number
        for x in nums1:
            if x % 2 == 1:
                min_odd = min(min_odd, x)

        # No odd numbers means all numbers are already even
        if min_odd == float('inf'):
            return True

        # If an even number exists, it must be greater
        # than the smallest odd number so we can make it odd.
        for x in nums1:
            if x % 2 == 0 and x <= min_odd:
                return False

        return True