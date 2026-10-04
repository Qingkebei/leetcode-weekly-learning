from typing import List, Optional


# 本地学习用节点定义；力扣已提供 TreeNode 时不需要重复提交。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """按左子树、根节点、右子树的顺序收集节点值。"""

        def dfs(node: Optional[TreeNode]) -> None:
            # 空节点没有值需要添加，结束当前调用。
            if node is None:
                return

            dfs(node.left)        # 完整处理左子树后，才继续执行下一句。
            ans.append(node.val)  # 访问当前节点。
            dfs(node.right)       # 完整处理右子树。

        # 定义 dfs 时不执行函数体；调用前创建 ans 即可。
        ans = []
        dfs(root)
        return ans


# 时间复杂度：O(n)。
# 辅助空间：O(h) 递归栈；另需 O(n) 保存输出，h 为树的高度。
