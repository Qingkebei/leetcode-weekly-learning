from typing import Optional


# 本地学习用节点定义；力扣已提供 TreeNode 时不需要重复提交。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False

            # 外侧对外侧、内侧对内侧，才能构成镜像。
            return (
                is_mirror(left.left, right.right)
                and is_mirror(left.right, right.left)
            )

        if root is None:
            return True
        return is_mirror(root.left, root.right)


# 时间复杂度 O(n)；递归栈 O(h)，h 为树高。
