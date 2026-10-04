from typing import Optional


# 本地学习用节点定义；力扣已提供 TreeNode 时不需要重复提交。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 保存以每个节点为路径最高点时，对应的路径边数。
        ans = []

        def f(node: TreeNode | None) -> int:
            # 这里用边数定义深度：空节点为 -1，叶子节点为 0。
            if node is None:
                return -1

            l_depth = f(node.left)
            r_depth = f(node.right)

            # 路径从左子树经过当前节点，再到右子树。
            depth = l_depth + r_depth + 2
            ans.append(depth)

            # 返回的是当前子树的深度，供父节点计算，不是直径。
            return max(l_depth, r_depth) + 1

        f(root)
        # 空树没有节点，ans 为空；default=0 保证此时返回 0。
        return max(ans, default=0)


# 时间复杂度：O(n)；列表与递归栈总额外空间：O(n)。
