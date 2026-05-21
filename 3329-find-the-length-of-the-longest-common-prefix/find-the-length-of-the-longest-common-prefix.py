class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        arr1_prefixes = set()  # Set to store all prefixes from arr1

        # Step 1: Build all possible prefixes from arr1
        for val in arr1:
            while val not in arr1_prefixes and val > 0:
                # Insert current value as a prefix
                arr1_prefixes.add(val)
                val //= 10

        longest_prefix = 0
        for val in arr2:
            while val not in arr1_prefixes and val > 0:
                val //= 10
            if val > 0:
                longest_prefix = max(longest_prefix, len(str(val)))

        return longest_prefix