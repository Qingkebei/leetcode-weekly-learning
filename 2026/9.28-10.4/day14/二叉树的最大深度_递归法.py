from typing import Optional


# 本地学习用节点定义；力扣已提供 TreeNode 时不需要重复提交。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """返回以 root 为根的子树的最大层数。"""

        # 空树深度为 0，供上一层参与数值计算。
        if root is None:
            return 0

        # 每层调用都有自己独立的 root、l_depth 和 r_depth。
        l_depth = self.maxDepth(root.left)
        r_depth = self.maxDepth(root.right)

        # 选较深的一边，再加上当前根节点这一层。
        return max(l_depth, r_depth) + 1


# 时间复杂度：O(n)。
# 辅助空间：O(h) 递归栈；最坏退化为单链时为 O(n)。
