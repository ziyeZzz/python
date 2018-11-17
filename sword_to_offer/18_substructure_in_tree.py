# -*- coding:utf-8 -*-
'''
Q: 树的子结构
输入两棵二叉树A和B，判断B是不是A的子结构。二叉树的结点的定义如下：
struct BinaryTreeNode
{
    int                 m_nValue;
    BinaryTreeNode*     m_pleft;
    BinaryTreeNode*     m_pRight;
}
'''
class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def add_left(self, dataOrNode):
        if not isinstance(dataOrNode, TreeNode):
            dataOrNode = TreeNode(dataOrNode)
        self.left = dataOrNode
    def add_right(self, dataOrNode):
        if not isinstance(dataOrNode, TreeNode):
            dataOrNode = TreeNode(dataOrNode)
        self.right = dataOrNode
    def __repr__(self):
        return str(self.data)

class Tree(object):
    def __init__(self):
        self.root = None
    def add_node(self, dataOrNode):
        #TODO unfinised tree related coding
        return