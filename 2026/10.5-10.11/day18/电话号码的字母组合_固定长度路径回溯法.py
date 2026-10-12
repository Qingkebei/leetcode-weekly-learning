from typing import List


MAPPING = "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []

        ans = []
        path = [""] * n

        def dfs(i: int) -> None:
            if i == n:
                ans.append("".join(path))
                return
            for c in MAPPING[int(digits[i])]:
                path[i] = c
                dfs(i + 1)

        dfs(0)
        return ans


# 根据本次对话中的代码整理；path 每层覆盖当前位置，无需 pop。
