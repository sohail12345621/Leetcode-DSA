class Solution:
    def partitionLabels(self, s):
        
        # store last occurrence of each character
        last = {}

        for i, ch in enumerate(s):
            last[ch] = i

        result = []

        start = 0
        end = 0

        for i, ch in enumerate(s):

            # extend partition end
            end = max(end, last[ch])

            # partition complete
            if i == end:

                result.append(end - start + 1)

                start = i + 1

        return result