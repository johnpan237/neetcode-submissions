"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = { None:None }
        cur = head

        # first pass, copy nodes
        while cur:
            new = Node(cur.val)
            oldToNew[cur] = new
            cur = cur.next
        
        # second pass, copy links
        cur = head
        while cur:
            new = oldToNew[cur]
            new.next = oldToNew[cur.next]
            new.random = oldToNew[cur.random]
            cur = cur.next
        
        return oldToNew[head]