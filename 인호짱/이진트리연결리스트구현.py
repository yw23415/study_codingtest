# 기존의 연결리스트에서 next 대신 right와 left 사용

from collections import deque

class Node:
    def __init__(self, value):
	    self.value = value
	    self.left = None
	    self.right = None

class Tree:
	def __init__(self, node):
		self.root = node

	# 디버그용
	def display(self):
		# level order
		queue = deque()
		queue.append(self.root)
		while queue:
			curr_node = queue.popleft()
			print(curr_node.value)
			if curr_node.left:
				queue.append(curr_node.left)
			if curr_node.right:
				queue.append(curr_node.right)

# 1
tree = Tree(Node(9))
# 2
tree.root.left = Node(3)
tree.root.right = Node(8)
# 3
tree.root.left.left = Node(2)
tree.root.left.right = Node(5)
tree.root.right.right = Node(7)
# 4
tree.root.left.right.right = Node(4)

print(tree.display())