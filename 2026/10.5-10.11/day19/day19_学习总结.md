---
title: "Day 19：贪心练习与 Trie 初识"
aliases:
  - "Day 19 学习总结"
tags:
  - LeetCode
  - Python
  - 贪心
  - Trie
  - day19
date: 2026-10-09
status: completed
---

# Day 19：贪心练习与 Trie 初识

今天记录三道贪心题：[[跳跃游戏_最远可达位置法.py|55. 跳跃游戏]]、[[跳跃游戏II_区间最远位置法.py|45. 跳跃游戏 II]]、[[买卖股票的最佳时机_最低价格法.py|121. 买卖股票的最佳时机]]；另学习并独立重写了 [[实现Trie前缀树_字典节点法.py|208. 实现 Trie]]。四份代码均按本次对话中收到的写法整理；未记录力扣提交结果。

## 55. 跳跃游戏

`max_reach` 表示目前能到达的最远下标。遍历到 `i` 时，先检查 `i > max_reach`：如果当前位置都到不了，就无法继续向右；否则用 `i + nums[i]` 扩大最远范围。

```python
if i > max_reach:
    return False
max_reach = max(max_reach, i + x)
if max_reach >= n - 1:
    return True
```

例如 `[3, 2, 1, 0, 4]`，前四个位置最多只能到下标 `3`，遍历到下标 `4` 时返回 `False`。时间 `O(n)`，额外空间 `O(1)`。题目保证数组非空；按这份写法，合法输入会在循环中返回结果。

## 45. 跳跃游戏 II

这题求**最少跳跃次数**。`cur_reach` 是使用当前步数能到达的最远边界；`right_reach` 是扫描当前可达范围时，发现再跳一步能到达的最远位置。走到当前边界 `i == cur_reach`，才需要将 `ans` 加一，并把下一轮边界更新为 `right_reach`。

```python
right_reach = max(right_reach, i + nums[i])
if i == cur_reach:
    cur_reach = right_reach
    ans += 1
```

例如 `[2, 3, 1, 1, 4]`：在 `i = 0`，第一跳的边界变成 `2`；扫描到 `i = 1` 时发现下一跳最远可到 `4`；走到当前边界 `i = 2`，第二跳的边界变成 `4`，答案为 `2`。循环只走到倒数第二个下标，避免已经站在终点时再多计一次。题目保证终点可达。时间 `O(n)`，额外空间 `O(1)`。

第 55 题只问能否到达，所以保存一个最远位置即可；第 45 题要数最少跳几次，因此还要区分当前步数的边界与下一步的最远位置。

## 121. 买卖股票的最佳时机

`min_price` 保存到今天为止见过的最低买入价。每看到当天价格 `p`，先用 `p - min_price` 更新最大利润 `ans`，再更新最低价格，供之后的日期使用。

```python
ans = max(ans, p - min_price)
min_price = min(min_price, p)
```

例如 `[7, 1, 5, 3, 6, 4]`，最低价降到 `1` 后，看到价格 `6` 时得到最大利润 `5`。`ans` 从 `0` 开始，因此持续下跌时返回 `0`。时间 `O(n)`，额外空间 `O(1)`。

共同点：遍历时只保存足以决定后续答案的信息；跳跃游戏保存可达范围，股票题保存历史最低买入价与当前最大利润。

## 208. 实现 Trie（前缀树）

今天先阅读了[灵茶山艾府的题解](https://leetcode.cn/problems/implement-trie-prefix-tree/solutions/2993894/cong-er-cha-shu-dao-er-shi-liu-cha-shu-p-xsj4/)中的参考代码，之后澄清了 `self` 的作用，并把用户自行重写、发到对话中的版本保存为 [[实现Trie前缀树_字典节点法.py|Trie 代码]]。粘贴内容里的 `**slots**` 是 Markdown 显示造成的格式错位，归档时还原为 Python 的 `__slots__`；`search` 和 `startsWith` 保留用户的 `if/else` 写法。

先只记核心画面：每个节点的 `son` 字典记录“下一个字母 → 下一个节点”，`end` 表示是否有一个完整单词恰好停在此处。例如插入 `app` 和 `apple`，两个单词共用 `a → p → p` 这段路；第三个 `p` 的 `end` 为 `True`，最后 `e` 的 `end` 也为 `True`。因此 `app` 是完整单词，`ap` 只是前缀。

阅读顺序：先看 `Node` 保存什么，再看 `insert` 如何造路，最后看 `find` 如何区分找不到路（`0`）、只有前缀（`1`）和完整单词（`2`）。`search` 检查 `find == 2`；`startsWith` 检查 `find != 0`。代码中的 `__init__` 是构造函数，`__slots__` 是可暂时跳过的内存优化。

### 今天澄清的 `self`

- 在 `Node.__init__(self)` 中，`self` 是新创建的那个节点；`self.son` 和 `self.end` 是该节点保存的数据。每次 `Node()` 都有自己的字典和结束标记。
- 在 `Trie.__init__(self)` 中，`self` 是当前 Trie 对象；`self.root = Node()` 给它保存一个长期可用的起点。
- 在 `Trie.insert(self, word)` 和 `Trie.find(self, word)` 中，`self` 仍是当前 Trie 对象；`cur = self.root` 取得起点，但 `cur` 只是本次调用中沿字母路径移动的临时变量。
- `search` 和 `startsWith` 中的 `self.find(...)` 表示让同一个 Trie 对象调用自己的查找方法。调用 `trie.insert("app")` 时，Python 会自动把 `trie` 传给 `insert` 的 `self`，调用处不必显式写 `self`。

学习状态：已收到并归档用户独立重写的代码；尚未记录力扣提交结果，按照用户偏好未做本地运行测试。
