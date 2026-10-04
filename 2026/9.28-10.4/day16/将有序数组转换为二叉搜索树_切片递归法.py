from typing import List, Optional


# 本地学习用节点定义；力扣已提供 TreeNode 时不需要重复提交。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 空数组没有节点，也是递归停止条件。
        if not nums:
            return None

        m = len(nums) // 2

        # [:m] 取中间元素左边；[m + 1:] 取中间元素右边。
        left = self.sortedArrayToBST(nums[:m])
        right = self.sortedArrayToBST(nums[m + 1:])

        # 两次递归各返回一棵子树的根节点。
        return TreeNode(nums[m], left, right)


# 时间复杂度 O(n log n)：每层切片复制数组。
# 额外空间 O(n)：切片与递归栈；不计返回的树节点。
