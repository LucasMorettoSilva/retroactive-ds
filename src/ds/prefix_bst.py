# class PrefixBST:
#
#     class Node:
#         def __init__(self, key, value, w):
#             self.value = value
#             self.left = None
#             self.right = None
#             self.left_height = 0
#             self.right_height = 0
#             self.left_count = 1
#             self.left_sum = value
#             self.right_count = 0
#             self.right_sum = 0
#             self.key = key
#             self.w = w
#
#         def set_value(self, value):
#             self.value = value
#             self.left_sum = self.left.left_sum + self.left.right_sum + self.value if self.left else self.value
#
#         def set_left(self, node):
#             self.left = node
#             self.left_height = max(node.left_height, node.right_height) + 1 if node else 0
#             self.left_count = node.left_count + node.right_count + 1 if node else 1
#             self.left_sum = node.left_sum + node.right_sum + self.value if node else self.value
#
#         def set_right(self, node):
#             self.right = node
#             self.right_height = max(node.left_height, node.right_height) + 1 if node else 0
#             self.right_count = node.left_count + node.right_count if node else 0
#             self.right_sum = node.left_sum + node.right_sum if node else 0
#
#         def rotate_left(self):
#             b = self.right
#             self.set_right(b.left)
#             b.set_left(self)
#             return b
#
#         def rotate_right(self):
#             a = self.left
#             self.set_left(a.right)
#             a.set_right(self)
#             return a
#
#         def factor(self):
#             return self.right_height - self.left_height
#
#     def __init__(self):
#         self.__root = None
#
#     def put(self, key, val, w):
#
#     def __put(self, x, key, val, w):
#         if x is None:
#             return self.Node(key, val, w)
#
#         if key < x.key:
#             x.set_left(add_node(x.left, key, node))
#             if root.factor() < -1:
#                 if root.left.factor() > 0:
#                     root.set_left(root.left.rotate_left())
#                 return root.rotate_right()
#         else:
#             root.set_right(add_node(root.right, key, node))
#             if root.factor() > 1:
#                 if root.right.factor() < 0:
#                     root.set_right(root.right.rotate_right())
#                 return root.rotate_left()
#
#         return root
#
#
# class Node:
#     def __init__(self, value, key):
#         self.value = value
#         self.left = None
#         self.right = None
#         self.left_height = 0
#         self.right_height = 0
#         self.left_count = 1
#         self.left_sum = value
#         self.right_count = 0
#         self.right_sum = 0
#         self.key = key
#
#     def set_value(self, value):
#         self.value = value
#         self.left_sum = self.left.left_sum + self.left.right_sum+self.value if self.left else self.value
#
#     def set_left(self, node):
#         self.left = node
#         self.left_height = max(node.left_height, node.right_height)+1 if node else 0
#         self.left_count = node.left_count + node.right_count+1 if node else 1
#         self.left_sum = node.left_sum + node.right_sum+self.value if node else self.value
#
#     def set_right(self, node):
#         self.right = node
#         self.right_height = max(node.left_height, node.right_height)+1 if node else 0
#         self.right_count = node.left_count + node.right_count if node else 0
#         self.right_sum = node.left_sum + node.right_sum if node else 0
#
#     def rotate_left(self):
#         b = self.right
#         self.set_right(b.left)
#         b.set_left(self)
#         return b
#
#     def rotate_right(self):
#         a = self.left
#         self.set_left(a.right)
#         a.set_right(self)
#         return a
#
#     def factor(self):
#         return self.right_height - self.left_height
#
# def add_node(root, key, node):
#     if root is None: return node
#
#     if key < root.key:
#         root.set_left(add_node(root.left, key, node))
#         if root.factor() < -1:
#             if root.left.factor() > 0:
#                 root.set_left(root.left.rotate_left())
#             return root.rotate_right()
#     else:
#         root.set_right(add_node(root.right, key, node))
#         if root.factor() > 1:
#             if root.right.factor() < 0:
#                 root.set_right(root.right.rotate_right())
#             return root.rotate_left()
#
#     return root
#
# def update_node(root, key, value):
#     if root is None: return root
#
#     if key < root.key:
#         root.set_left(update_node(root.left, key, value))
#     elif key > root.key:
#         root.set_right(update_node(root.right, key - root.left_count, value))
#     else:
#         root.set_value(value)
#
#     return root
#
#
# def prefix_sum(root, key):
#     if root is None: return 0
#
#     if key < root.key:
#         return prefix_sum(root.left, key)
#     else:
#         return root.left_sum + prefix_sum(root.right, key)
