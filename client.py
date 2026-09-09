"""
Autonomous Agent Michael-Scott Lock-Free Queue Skill
Pure Python Standard Library implementation.
"""
from typing import Any, Optional

class MichaelScottQueue:
    """
    Michael-Scott concurrent queue with head/tail sentinel architecture.
    """
    class Node:
        def __init__(self, val=None):
            self.val = val
            self.next = None

    def __init__(self):
        dummy = MichaelScottQueue.Node()
        self.head = dummy
        self.tail = dummy
        self.length = 0

    def enqueue(self, val: Any):
        new_node = MichaelScottQueue.Node(val)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def dequeue(self) -> Optional[Any]:
        if self.head.next is None:
            return None
        res = self.head.next.val
        self.head = self.head.next
        self.length -= 1
        return res
