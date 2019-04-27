'''
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
'''
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.lef=None
        self.right=None

# 迭代
def isSymmetric(root):
    parentList = [root]
    while parentList:
        childList = []
        # 把下一层的孩子节点都加入
        for node in parentList:
            if node:
                childList +=[node.left, node.right]
        # 看孩子节点的值是否对称相等
        for i in range(len(childList)//2):
            # childList有一个为None; childList都不为None但值不相等
            if (childList[i]==None and childList[-i-1]!=None) or (childList[i]!=None and childList[-i-1]==None):
                return False
            if childList[i] and childList[-i-1] \
                    and childList[i].val != childList[-i-1].val:
                return False
        parentList = childList
    return True

# 递归
def isSymmetric2(root):
    return ismirror(root,root)
def ismirror(p,q):
    # p,q都为None
    if not p and not q:
        return True
    # p,q有一个为None
    if not p or not q:
        return False
    if(p.val == q.val):
        return ismirror(p.left,q.right) and ismirror(p.right,q.left)
    return False








