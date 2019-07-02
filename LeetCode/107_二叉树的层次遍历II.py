'''
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
'''
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
def levelOrderBottom(root):
    if not root:
        return []
    parentList = [root]
    result=[]
    while parentList:
        childList = []
        childListVal = []
        for node in parentList:
            childListVal.append(node.val)
            if node.left:
                childList.append(node.left)
            if node.right:
                childList.append(node.right)
        result.append(childListVal)
        parentList = childList
    return result[::-1]