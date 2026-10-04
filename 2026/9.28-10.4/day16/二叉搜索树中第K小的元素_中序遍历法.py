from typing import Optional


# 本地学习用节点定义；力扣已提供 TreeNode 时不需要重复提交。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal k, ans

            if node is None or k == 0:
                return

            dfs(node.left)

            # 答案可能已经在左子树找到；不要再减小 k。
            if k == 0:
                return

            k -= 1
            if k == 0:
                ans = node.val
                return

            dfs(node.right)

        dfs(root)
        return ans


# 中序遍历二叉搜索树会按从小到大访问节点。
# 时间复杂度 O(h + k)，最坏 O(n)；额外空间 O(h) 递归栈。
