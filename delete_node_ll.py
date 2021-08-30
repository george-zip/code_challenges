"""
Leet Code Problem 237: Delete node from linked list given the 
node itself.
"""

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def make_linked_list(nodes: List[int]) -> ListNode:
	"""
	Construct linked list from list of integers and return head
	"""
	current = None
	while nodes:
		tmp = ListNode(nodes.pop())
		tmp.next = current
		current = tmp
	return current


def print_linked_list(head):
	while head:
		print(head.val)
		head = head.next


class Solution:
	def deleteNode(self, node):
		# take on value of next node 
		# garbage collection will take care of memory used
		# next_node
		next_node = node.next
		node.val = next_node.val
		node.next =	next_node.next
				


head = make_linked_list([4,5,1,9])
print("Before deletion:")
print_linked_list(head)
dead_node = head.next
sol = Solution()
sol.deleteNode(dead_node)
print("After deletion:")
print_linked_list(head)