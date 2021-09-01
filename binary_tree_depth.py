"""
Leet code 104: Maximum Depth of Binary Tree
Straighforward recursive approach
Obviously, the size of the binary tree is fairly
limited, but this is a very easy-to-understand solution.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def create_binary_tree(nodes, idx=0):
	"""
	Construct binary tree from list of nodes
	If the parent node is at index i,
	then the left child of that node is at (2*i + 1)
	and right child is at (2*i + 2).
	Return root node
	"""
	root = None
	if idx < len(nodes) and nodes[idx] != 'null':
		root = TreeNode(
			nodes[idx],
			create_binary_tree(nodes, idx * 2 + 1),
			create_binary_tree(nodes, idx * 2 + 2)
		)
	return root


class Solution:
	def maxDepth(self, root: Optional[TreeNode]) -> int:
		depth = 0
		if root:
			return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
		return depth


root = create_binary_tree([1])
print(root.val)
root = create_binary_tree([1, "null", 2])
print(root.val, root.left, root.right.val)
root = create_binary_tree([3, 9, 20, "null", "null", 15, 7])
print(root.val, root.left.val, root.right.val, root.right.right.val)

sol = Solution()
print(sol.maxDepth(create_binary_tree([1])))
print(sol.maxDepth(create_binary_tree([3, 9, 20, "null", "null", 15, 7])))
print(sol.maxDepth([]))
