# -*- coding:utf-8 -*-
'''
Q：二叉树的镜像
请完成一个函数，输入一个二叉树，该函数输出它的镜像。
'''
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None
    def __repr__(self):
        return self.data
    # def get_child_num(self):
    #     if self.left_node == None:
    #         return 0
    #     elif self.right_node == None:
    #         return 1
    #     else: return 2

class binary_tree(object):
    def __init__(self, root):
        if not isinstance(root, Node):
            root = Node(root)
        self.root = root

    def add_node(self, parent_node, dataOrNode):
        node = self.root
        if node.

