---
title: "Day 15：二叉树的直径、层序遍历与结构比较"
aliases:
  - "Day 15 学习总结"
tags:
  - LeetCode
  - Python
  - 二叉树
  - 递归
  - 广度优先搜索
  - day15
date: 2026-10-02
status: completed
---

# Day 15：二叉树的直径、层序遍历与结构比较

本日题目：

1. [[二叉树的直径_递归深度法.py|543. 二叉树的直径]]
2. [[二叉树的层序遍历_队列法.py|102. 二叉树的层序遍历：队列法]]
3. [[二叉树的层序遍历_逐层列表法.py|102. 二叉树的层序遍历：自己写的 cur / nxt 法]]
4. [[二叉树的右视图_层序遍历法.py|199. 二叉树的右视图]]
5. [[相同的树_递归法.py|100. 相同的树]]
6. [[对称二叉树_镜像递归法.py|101. 对称二叉树]]

## 思路：递归返回深度，列表记录直径候选值

直径指任意两个节点之间最长路径的**边数**，这条路径不一定经过整棵树的根节点。

对每个节点，分别求左右子树深度。这里用边数定义深度，因此空节点返回 `-1`，叶子节点深度为 `0`：

```python
if node is None:
    return -1

l_depth = f(node.left)
r_depth = f(node.right)
```

经过当前节点、连通左右两侧的路径边数为：

```python
depth = l_depth + r_depth + 2
ans.append(depth)
```

例如叶子节点的左右子树都为空，得到 `-1 + -1 + 2 = 0`。若左子树深度为 `1`、右子树深度为 `0`，经过当前节点的路径为 `1 + 0 + 2 = 3` 条边。

递归函数 `f(node)` 向父节点返回的是**当前子树的深度**：

```python
return max(l_depth, r_depth) + 1
```

它不能把当前节点的直径直接返回给父节点，因为父节点需要知道“从这个孩子出发最多能向下走多远”。整棵树的答案则从所有节点的候选路径中选最大值。

## `max(ans, default=0)` 与原代码的错误

```python
f(root)
return max(ans, default=0)
```

`ans` 是列表，`max(ans)` 才是在列表中取最大值。`f(root)` 返回一个整数深度，不能把它传给 `max` 当成列表。空树时 `ans` 为空，`default=0` 让答案为 0；直接 `max([])` 会报错。

## 列表、`nonlocal` 和 `global`

你当前的 `ans = []` 位于 `diameterOfBinaryTree` 内。内层函数执行 `ans.append(depth)` 是修改已有的同一个列表，没有给变量 `ans` 重新赋值，所以不需要 `nonlocal`。

如果想只用一个整数保存当前最大值，可以这样写：

```python
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    ans = 0

    def f(node: TreeNode | None) -> int:
        nonlocal ans
        if node is None:
            return -1

        l_depth = f(node.left)
        r_depth = f(node.right)
        ans = max(ans, l_depth + r_depth + 2)
        return max(l_depth, r_depth) + 1

    f(root)
    return ans
```

`nonlocal ans` 表示修改外层 `diameterOfBinaryTree` 中的变量 `ans`。这里的 `ans` 是**外层局部变量**，不是全局变量。

真正的全局变量写在所有函数和类之外，在函数内重新赋值时使用 `global ans`。本题每次调用都应重新从 0 开始，因此使用外层局部变量与 `nonlocal` 更合适。

## 两种写法的取舍

- **列表写法**：贴近你自己推导的过程；保存每个节点算出的候选路径，最后用 `max`。额外列表空间为 `O(n)`。
- **整数写法**：递归过程中不断更新最大值，不保存全部候选路径；额外空间只有递归栈 `O(h)`，`h` 为树高。

两种写法都遍历每个节点一次，时间复杂度均为 `O(n)`。这里的 `TreeNode | None` 表示节点或空值，要求 Python 3.10+；`Optional[TreeNode]` 表达相同含义。

## 层序遍历：用队列按层处理

层序遍历先处理根节点，再处理第二层、第三层。队列先进入的节点先出来：

```python
queue = deque([root])
node = queue.popleft()  # 取出队列最左端的节点
queue.append(node.left)  # 左孩子排到队尾，等待下一层处理
```

每一轮 `while queue` 开始时，队列中正好是当前层的节点。先记录：

```python
level_size = len(queue)
```

随后只取出 `level_size` 个节点；它们的孩子虽然加入队尾，但要等下一轮才处理。这样每一层形成一个列表。例如：

```text
    1
   / \
  2   3
 /
4
```

结果为 `[[1], [2, 3], [4]]`。空树直接返回 `[]`。

自己写的另一种 BFS 用两个列表明确分层：`cur` 保存当前层，`nxt` 收集下一层，`values` 保存当前层的数值。处理完整层后执行 `ans.append(values)` 和 `cur = nxt`；下一轮便处理下一层。它不需要 `popleft()`，也不需要预先保存 `level_size`。两种写法均为 `O(n)` 时间。

## 右视图：取每层最右边的节点

继续用同样的层序遍历，保持“先左孩子、后右孩子”的入队顺序。这样当前层最后出队的节点，就是这一层从右边看到的节点：

```python
for i in range(level_size):
    node = queue.popleft()
    if i == level_size - 1:
        answer.append(node.val)
```

在上面的树中，右视图是 `[1, 3, 4]`。第三层虽然只有左侧的节点 `4`，从右边看仍能看见它；所以不能只沿着 `root.right` 一直向下走。

这两题都是 `O(n)` 时间。队列可能存放一整层的节点，占用最多 `O(n)` 额外空间。

## 相同的树：同位置比较

`isSameTree(p, q)` 的含义是：判断以 `p`、`q` 为根的两棵子树是否完全相同。

1. 两个节点都是 `None`：当前位置相同，返回 `True`。
2. 只有一个是 `None`，或两个值不同：返回 `False`。
3. 当前值相同：继续比较左与左、右与右。

```python
return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
```

只有值相等还不够，左右连接的位置也必须一样。

## 对称二叉树：镜像位置比较

对称指根节点左右两棵子树互为镜像。边界判断与“相同的树”类似，但递归配对方式不同：

```text
左子树的左孩子  ↔  右子树的右孩子（外侧）
左子树的右孩子  ↔  右子树的左孩子（内侧）
```

```python
return (
    is_mirror(left.left, right.right)
    and is_mirror(left.right, right.left)
)
```

例如 `[1, 2, 2, 3, 4, 4, 3]` 所表示的树是对称的。空树也按对称处理，返回 `True`。

“相同的树”和“对称二叉树”都最多检查每个节点一次，时间复杂度 `O(n)`；递归栈空间 `O(h)`，`h` 为树高。
