class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            g[b].append(a)

        colors = [0] * numCourses

        def dfs(x: int) -> bool:
            colors[x] = 1
            for y in g[x]:
                if colors[y] == 1 or (colors[y] == 0 and dfs(y)):
                    return True
            colors[x] = 2
            return False

        for i, c in enumerate(colors):
            if c == 0 and dfs(i):
                return False
        return True


# 根据本次对话中的代码整理。dfs 返回 True 表示发现环。
