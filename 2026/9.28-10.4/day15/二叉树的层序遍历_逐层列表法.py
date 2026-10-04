from typing import List, Optional


# 本地学习用节点定义；力扣已提供 TreeNode 时不需要重复提交。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """使用当前层 cur 和下一层 nxt，逐层收集节点值。"""

        if root is None:
            return []

        ans = []
        cur = [root]

        while cur:
            nxt = []
            values = []

            for node in cur:
                values.append(node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)

            ans.append(values)
            cur = nxt

        return ans


# 时间复杂度 O(n)；不计答案时，cur 和 nxt 的空间为 O(w)，w 为最大层宽。
