# import self as self
#
#
# class TreeNode:
#     node_id: int
#     node_parent: "TreeNode"
#     node_children: ["TreeNode"]
#
#     def __init__(self, node_id: int, parent: "TreeNode" = None):
#         self.node_id = node_id
#         self.parent = parent
#         self.children = []
#
#
# class BinaryTree:
#
#     __root: TreeNode
#     __node_count: int
#
#     def __init__(self):
#         self.__root = TreeNode(-1)
#         self.__node_count = 1
#
#     def add_node_by_list_at_node(self, input_list: [int], node: TreeNode):
#         if len(input_list) > 0:
#             for child in node.children:
#                 if child.node_id ==  node.node_id:
#
#                 self.add_node_by_list_at_node(input_list[1:], node)
#
#
# newTree = BinaryTree()
# pass


print("hello python")