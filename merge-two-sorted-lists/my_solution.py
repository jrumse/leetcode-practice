class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Base Cases: We've reached the end of a list
        if list1 == None:
            return list2
        if list2 == None: 
            return list1
        
        # New Node
        node = ListNode()
        
        # Assign Lowest node, recursively call merge with the lowest node's list iterated
        if list1.val <= list2.val:
            node = list1
            node.next = self.mergeTwoLists(list1.next, list2)
        else:
            node = list2
            node.next = self.mergeTwoLists(list1, list2.next)
        
        # return new node value
        return node