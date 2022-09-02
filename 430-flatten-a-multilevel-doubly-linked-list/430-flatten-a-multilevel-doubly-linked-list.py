"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head: return head
        
        # this is needed to  point to the head
        # what if the head has a child
        dummy = Node()
        curr, stack = dummy, [head]
        
        # loop while stack is there
        while stack:
            popped_node = stack.pop()
            
            # first add next and then the child
            # child needs to be popped earlier
            if popped_node.next: stack.append(popped_node.next)
            if popped_node.child: stack.append(popped_node.child)
                
            '''
            now fix the pointers
            1. dummy next is head
            2. head prev is dummy
            3. child of popped node is now stored in the stack -> mark as none
            4. move the pointer forward
            '''
            curr.next = popped_node
            popped_node.prev = curr
            popped_node.child = None
            curr = popped_node
        
        # head.prev shouldnt point back
        dummy.next.prev = None
        return dummy.next