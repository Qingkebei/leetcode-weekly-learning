from collections import deque
from typing import List, Optional


# 本地学习用节点定义；力扣已提供 TreeNode 时不需要重复提交。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        answer = []
        queue = deque([root])

        while queue:
            # 先固定本层节点数，避免新加入的下一层节点被提前处理。
            level_size = len(queue)
            level_values = []

            for _ in range(level_size):
                node = queue.popleft()  # 从队列左端取出本层节点。
                level_values.append(node.val)

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            answer.append(level_values)

        return answer


# 时间复杂度 O(n)；队列与答案最多占 O(n) 空间。
