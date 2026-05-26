class Solution:
    def jump(self, nums):
        jumps = 0
        current_end = 0
        farthest = 0

        # no need to go till last index
        for i in range(len(nums) - 1):

            # update farthest reachable index
            farthest = max(farthest, i + nums[i])

            # when current jump range ends
            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps