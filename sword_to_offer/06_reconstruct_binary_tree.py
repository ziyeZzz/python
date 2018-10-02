#-*- coding: utf-8 -*-
# 此题主要是 树，前序遍历，中序遍历
# 树的实现，遍历，重构
'''
Q: 重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如
输入前序遍历序列｛1，2，4，7，3，5，6，8｝和中序遍历序列｛4，7，2，1，5，3，8，6｝，
则重建出如图所示的二叉树并输出它的头结点。
    1
   / \
  2   3
 /   / \
4   5   6
 \     /
  7   8
注：前序：根>左>右
    中序：左>根>右
    后续：左>右>根
'''
class tree_node(object):
    def __init__(self, data):
        self.data = data
        self._left_child = None
        self._right_child = None

    def __repr__(self):
        return str(self.data)

class binary_tree(object):
    def __init__(self, dataOrNode):
        if isinstance(dataOrNode, tree_node):
            self.root = dataOrNode
        else:
            self.root = tree_node(dataOrNode)

    def add_left_child(self, parent_node, dataOrNode):
        if parent_node._left_child == None:
            return 'Error: already has left child.'

        if isinstance(dataOrNode, tree_node):
            parent_node._left_child = dataOrNode
        else:
            parent_node._left_child = tree_node(dataOrNode)

    def add_right_child(self, parent_node, dataOrNode):
        if parent_node._right_child == None:
            return 'Error: already has right child.'

        if isinstance(dataOrNode, tree_node):
            parent_node._right_child = dataOrNode
        else:
            parent_node._right_child = tree_node(dataOrNode)

    # def breadth_first_print(self):
    #


def reconstruct_binaryTree(tree, pre_order_list, mid_order_list):
    if len(pre_order_list)>0 and len(mid_order_list)>0:
        root = pre_order_list[0]
        if tree == None:
            tree = binary_tree(root)

        root_index = find_index(root, mid_order_list)
        left_child_tree = mid_order_list[:root_index]
        right_child_tree = mid_order_list[root_index+1:]


    else:
        return 'Error:'


def find_index(m, list):
    index = -1
    for i in range(0, len(list)):
        if list[i] == m:
            index = i
    return index



if __name__=='__main__':
    print('QAQ')