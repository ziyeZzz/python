'''
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
'''
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def isSameTree(p,q):
    # 如果p和q都是None
    if p == q:
        return True
    # 如果p和q都不为None,并且p的值等于q
    if p and q and p.val==q.val:
        # 递归判断左右子树是不是相等，只要有一个不相等就返回False
        if not isSameTree(p.left,q.left) or not isSameTree(p.right,q.right):
            return False
        # 只有递归全为True才会返回True
        else:
            return True
    else:
        return False
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)
print(isSameTree(p,q))
