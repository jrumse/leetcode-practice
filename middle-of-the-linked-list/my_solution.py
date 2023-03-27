class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # define
        length = 0
        midpoint = 0
        traverse = head
        iterator = 0
    
        # calculate length
        while traverse:
            length += 1
            traverse = traverse.next
        
        # Define again
        midpoint = (length // 2)
        traverse = head

        while iterator < midpoint:
            traverse = traverse.next
            iterator += 1
        
        return traverse