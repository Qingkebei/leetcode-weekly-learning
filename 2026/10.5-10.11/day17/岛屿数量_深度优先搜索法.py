from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i: int, j: int) -> None:
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
                return

            grid[i][j] = "2"
            dfs(i, j - 1)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i + 1, j)

        ans = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == "1":
                    dfs(i, j)
                    ans += 1
        return ans


# 根据本次讨论中的代码整理；尚未记录独立重写或力扣提交。
# DFS 会原地把已经访问的陆地从 "1" 改为 "2"。
