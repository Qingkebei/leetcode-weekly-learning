from typing import List, Optional


# 本地学习用节点定义；力扣已提供 TreeNode 时不需要重复提交。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.dfs(nums, 0, len(nums) - 1)

    def dfs(self, nums: List[int], lo: int, hi: int) -> Optional[TreeNode]:
        # lo、hi 都包含在当前范围中；lo > hi 说明范围为空。
        if lo > hi:
            return None

        # 偶数长度时选择中间偏左的元素。
        mid = lo + (hi - lo) // 2
        root = TreeNode(nums[mid])

        # 共用同一个 nums，只调整递归处理的下标范围。
        root.left = self.dfs(nums, lo, mid - 1)
        root.right = self.dfs(nums, mid + 1, hi)
        return root


# 时间复杂度 O(n)；额外空间 O(log n) 递归栈，不计返回的树节点。
