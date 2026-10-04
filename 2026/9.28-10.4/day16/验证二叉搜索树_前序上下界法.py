from math import inf
from typing import Optional


# 本地学习用节点定义；力扣已提供 TreeNode 时不需要重复提交。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(
        self,
        root: Optional[TreeNode],
        left: float = -inf,
        right: float = inf,
    ) -> bool:
        # 空子树不会违反二叉搜索树的规则。
        if root is None:
            return True

        x = root.val

        # 当前节点必须严格落在祖先传下来的范围内。
        # 左子树上界变成 x；右子树下界变成 x。
        return (
            left < x < right
            and self.isValidBST(root.left, left, x)
            and self.isValidBST(root.right, x, right)
        )


# 时间复杂度 O(n)；额外空间 O(h) 递归栈，h 为树高。
