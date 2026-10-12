class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        max_reach = 0

        for i, x in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + x)
            if max_reach >= n - 1:
                return True


# 根据本次对话中的写法整理；题目保证 nums 非空。
