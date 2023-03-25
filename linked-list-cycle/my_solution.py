class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Catch empty array
        if head == None:
            return False
        # Set slow iterator and fast iterator
        tortoise = head
        hare = head
        # While fast iterator doesn't reach the end of the list
        # if the end of the list is reached, there is no cycle, return False
        while hare.next and hare.next.next:
            # iterate slow by 1 and fast by 2
            tortoise = tortoise.next
            hare = hare.next.next
            # the tortoise and the hare alg shows that in a cycle eventually the slow iterator
            # and the fast iterator will meet. If this happens, there is a cycle, return True
            if tortoise == hare:
                return True
        
        return False
