# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first_index = -1
        prev_index =-1

        prev_node = head
        curr_node = head.next
        
        idx = 1
        mini_dist = float('inf')

        while (curr_node.next):
            if(curr_node.val > prev_node.val and curr_node.val > curr_node.next.val ) or (curr_node.val < prev_node.val and curr_node.val < curr_node.next.val):
                if first_index == -1 :
                    first_index = idx
                else:
                    mini_dist = min(mini_dist, idx - prev_index)
                prev_index = idx
            
            prev_node = curr_node
            curr_node = curr_node.next
            idx += 1
        if (first_index == -1 or prev_index == first_index ):
            return [-1,-1]
        max_dist = prev_index - first_index
        return [mini_dist, max_dist]
                