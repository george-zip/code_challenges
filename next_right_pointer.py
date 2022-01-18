"""
Leet code 108: Populating Next Right Pointers in Each Node
"""
from typing import List, Optional


class Node:
    """
    Node class

    Attributes:
        val: Value contained in this node
        left: Left child
        right: Right child
        next: Right next node
    """

    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def create_binary_tree(nodes: List[int], idx: int = 0) -> Node:
    """
    Construct binary tree from list of nodes
    If the parent node is at index i,
    then the left child of that node is at (2*i + 1)
    and right child is at (2*i + 2).
    Args:
        nodes: List of nodes
        idx: start index

    Returns:
        None
    """
    root = None
    if idx < len(nodes) and nodes[idx] != 'null':
        root = Node(
            nodes[idx],
            create_binary_tree(nodes, idx * 2 + 1),
            create_binary_tree(nodes, idx * 2 + 2)
        )
    return root


def add_right_pointer(target_node: Node, siblings: List[Node]) -> List[Node]:
    if target_node:
        if siblings:
            target_node.next = siblings.pop()
        siblings.extend(add_right_pointer(target_node.right, siblings))
        siblings.extend(add_right_pointer(target_node.left, siblings))
        siblings.append(target_node)
        return siblings
    else:
        return []


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        add_right_pointer(root, [])


nodes = [26, 30, 18, 16, 23, 19, 50, 15, 27, 29, 29, 2, 29, 6, 25, 42, 14, 16, 34, 31, 47, 27, 9, 15, 26, 15, 28, 38,
         40, 14, 29]
root = create_binary_tree(nodes)
traversed = add_right_pointer(root, [])
print(root.left.left.next.val)
print(root.left.right.next.val)
print(root.right.left.next.val)
print(root.right.right.next)
