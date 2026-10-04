from typing import Optional


# 本地学习用节点定义；力扣已提供 TreeNode 时不需要重复提交。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """原地翻转以 root 为根的子树，并返回其根节点。"""

        # 空树翻转后仍然为空，返回 None 供上一层连接。
        if root is None:
            return None

        # left、right 保存翻转后子树的根节点引用，不是节点值。
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # 两边都处理完成后，交换当前节点的左右连接。
        root.left = right
        root.right = left
        return root


# 时间复杂度：O(n)。
# 辅助空间：O(h) 递归栈；直接修改原节点连接，不创建新树。
