class Solution:
    def nodesBetweenCriticalPoints(self, head):
        # Need at least 3 nodes to have a critical point
        if head is None or head.next is None or head.next.next is None:
            return [-1, -1]

        prev = head
        curr = head.next
        pos = 1

        first = -1
        last = -1
        min_dist = float('inf')

        while curr.next:
            next_node = curr.next

            # Check if curr is a local maximum or local minimum
            is_max = curr.val > prev.val and curr.val > next_node.val
            is_min = curr.val < prev.val and curr.val < next_node.val

            if is_max or is_min:
                if first == -1:
                    # First critical point
                    first = pos
                else:
                    # Distance from previous critical point
                    min_dist = min(min_dist, pos - last)

                last = pos

            prev = curr
            curr = next_node
            pos += 1

        # Fewer than two critical points
        if first == -1 or first == last:
            return [-1, -1]

        # Maximum distance is between first and last critical points
        max_dist = last - first

        return [min_dist, max_dist]