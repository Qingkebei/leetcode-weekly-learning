from typing import Optional


# 本地学习用节点定义；力扣已提供 TreeNode 时不需要重复提交。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self,
        root: Optional[TreeNode],
        p: TreeNode,
        q: TreeNode,
    ) -> Optional[TreeNode]:
        # is 比较的是节点身份；p 或 q 本身也可能是公共祖先。
        if root is None or root is p or root is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 两边各找到一个目标节点，说明当前 root 是分叉处。
        if left is not None and right is not None:
            return root
        if left is not None:
            return left
        return right


# 题目保证 p、q 都在树中。时间 O(n)，递归栈 O(h)。
