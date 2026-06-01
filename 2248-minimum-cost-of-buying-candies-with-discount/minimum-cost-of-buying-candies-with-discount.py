class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # Sort in descending order
        cost.sort(reverse=True)

        total = 0

        # Traverse the array
        for i in range(len(cost)):
            
            # Every 3rd candy is free
            if (i + 1) % 3 != 0:
                total += cost[i]

        return total