class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If List is Empty
        if head == None:
            return head

        # Delcare List Stack
        listStack = []

        # Iterate through Linked List
        while head:
            listStack.append(head)
            head = head.next

        # Decalare new head from the top of the stack
        # Declare Traversal node
        newHead = listStack.pop()
        traversalNode = newHead

        while listStack:
            # Grab next node from the top
            newNode = listStack.pop()
            # Set next to none to prevent accidental cycle
            newNode.next = None
            # Set traversal node's next to the node at the top of the stack
            traversalNode.next = newNode
            # iterate
            traversalNode = traversalNode.next
            
        return newHead