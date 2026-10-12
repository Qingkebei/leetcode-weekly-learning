class Solution:
    def jump(self, nums: list[int]) -> int:
        ans = 0
        cur_reach = 0
        right_reach = 0

        for i in range(len(nums) - 1):
            right_reach = max(right_reach, i + nums[i])
            if i == cur_reach:
                cur_reach = right_reach
                ans += 1
        return ans


# 根据本次对话中的写法整理；题目保证可以到达最后一个位置。
