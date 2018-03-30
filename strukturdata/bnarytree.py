class Node:
	def __init__(self, val):
		self.leftChild = None
		self.rightChild = None
		self.data = val

def binary_insert(root, node):
	if root is None:
		root = node
	else:
		if root.data > node.data:
			if root.leftChild is None:
				root.leftChild = node
			else:
				binary_insert(root.leftChild, node)
		else:
			if root.rightChild is None:
				root.rightChild = node
			else:
				binary_insert(root.rightChild, node)

def in_order_print(root):
	if not root:
		return
	in_order_print(root.leftChild)
	print(root.data)
	in_order_print(root.rightChild)

def pre_order_print(root):
	if not root:
		return
	print(root.data)
	pre_order_print(root.leftChild)
	pre_order_print(root.rightChild)


r = Node(7)
binary_insert(r, Node(3))
binary_insert(r, Node(5))
binary_insert(r, Node(2))
binary_insert(r, Node(1))
binary_insert(r, Node(4))
binary_insert(r, Node(6))
binary_insert(r, Node(7))

print("in order")
in_order_print(r)

print("pre order")
pre_order_print(r)




# class BinarySearchTree:
# 	def __init__(self):
# 		self.root = root
# 		self.size = size

# 	def length(self):
# 		return self.size

# 	def __len__(self):
# 		return self.size

# 	def __iter__(self):
# 		return self.root.__iter__()


# class TreeNode:
# 	def __init__(self, key, val, left=None, right=None, parent=None):
# 		self.key = key
# 		self.val = val
# 		self.leftChild = self.left
# 		self.rightChild = self.right
# 		self.parent = parent

# 	def hashLeftChild(self):
# 		return self.leftChild

# 	def hashRightChild(self):
# 		return self.rightChild

# 	def isLeftChild(self):
# 		return self.parent and self.parent.leftChild == self

# 	def isRightChild(self):
# 		return self.parent and self.parent.rightChild == self

# 	def isRoot(self):
# 		return not (self.rightChild or self.leftChild)

# 	def isLeaf(self):
# 		return not (self.rightChild or self.leftChild)

# 	def hashAnyChildren(self):
# 		return self.rightChild or self.leftChild

# 	def hashBothChildren(self):
# 		return self.rightChild and self.leftChild

# 	def replaceNodeData(self):
# 		self.key = key
# 		self.payload = value
# 		self.leftChild = lc
# 		self.rightChild = rc
# 		if self.hashLeftChild():
# 			self.leftChild.parent = self
# 		if self.hashRightChild():
# 			self.rightChild.parent = self




