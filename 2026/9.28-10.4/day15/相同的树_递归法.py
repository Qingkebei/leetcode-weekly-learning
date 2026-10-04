from typing import Optional


# 本地学习用节点定义；力扣已提供 TreeNode 时不需要重复提交。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(
        self, p: Optional[TreeNode], q: Optional[TreeNode]
    ) -> bool:
        # 两边都为空，当前这一对位置相同。
        if p is None and q is None:
            return True

        # 只有一边为空，或两个节点的值不同，都不是相同的树。
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False

        # 两棵树对应位置必须同时相同。
        return (
            self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )


# 时间复杂度 O(n)，n 为比较到的节点数；递归栈 O(h)。
