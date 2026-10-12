# 学习时参考灵茶山艾府的力扣题解：
# https://leetcode.cn/problems/implement-trie-prefix-tree/solutions/2993894/cong-er-cha-shu-dao-er-shi-liu-cha-shu-p-xsj4/
# 本文件记录用户在理解后自行重写并发到对话中的版本。


class Node:
    __slots__ = 'son', 'end'

    def __init__(self):
        self.son = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.son:
                cur.son[c] = Node()
            cur = cur.son[c]
        cur.end = True

    def find(self, word: str) -> int:
        cur = self.root
        for c in word:
            if c not in cur.son:
                return 0
            cur = cur.son[c]
        return 2 if cur.end else 1

    def search(self, word: str) -> bool:
        if self.find(word) == 2:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        if self.find(prefix) != 0:
            return True
        else:
            return False
