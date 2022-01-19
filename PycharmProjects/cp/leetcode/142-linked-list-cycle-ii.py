# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # space, time = O(N)

        seen = set()
        count = 0
        cur = head
        while cur:
            if cur not in seen:
                seen.add(cur)
            else:
                return cur

            cur = cur.next
        return None