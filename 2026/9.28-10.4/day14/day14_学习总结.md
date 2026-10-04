---
title: "Day 14：二叉树基础与三个递归"
aliases:
  - "Day 14 学习总结"
tags:
  - LeetCode
  - Python
  - 二叉树
  - 递归
  - day14
date: 2026-10-02
study_dates:
  - 2026-10-01
  - 2026-10-02
status: completed
---

# Day 14：二叉树基础与三个递归

本次学习跨 10 月 1 日至 2 日，统一归入 day14。

1. [[二叉树的中序遍历_递归法.py|94. 二叉树的中序遍历]]
2. [[二叉树的最大深度_递归法.py|104. 二叉树的最大深度]]
3. [[翻转二叉树_递归法.py|226. 翻转二叉树]]

## 一、二叉树节点与子树

每个节点最多有两个子节点，分别用 left、right 引用：

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

- val：当前节点的值。
- left、right：左右子节点；不存在时为 None。
- root：整棵树或某一棵子树的根节点。
- 叶子节点：左右孩子都为 None 的节点。

普通二叉树不要求节点值满足大小关系。二叉搜索树才有左子树较小、右子树较大的有序性质（重复值的约定需看具体定义）。

```text
    1
   / \
  2   3
 /
4
```

以 2 为根的子树包含节点 2、4。大树的左右子树仍然具有同样的结构，所以可以用同一个函数递归处理。

## 二、dfs 括号里的内容是什么

定义函数：

```python
def dfs(node: Optional[TreeNode]) -> None:
```

node 是接收输入的参数；Optional[TreeNode] 是类型提示，表示节点或 None。它也可以写成 TreeNode | None（Python 3.10+）。

调用函数：

```python
dfs(root)        # 传入整棵树的根节点
dfs(node.left)   # 传入当前节点的左孩子
dfs(node.right)  # 传入当前节点的右孩子
```

传入的是节点引用，不会复制一棵树。每次调用都有独立的局部参数 node：

```text
第一层 node 指向节点 1
第二层 node 指向节点 2
第三层 node 指向节点 4
第四层 node 是 None，返回上一层
```

下一层返回后，上一层继续从调用语句后面执行；上一层的 node 仍指向它原来的节点。

dfs 定义在 inorderTraversal 内部，是局部函数，直接写 dfs(...)。maxDepth 和 invertTree 是 Solution 的实例方法，因此用 self.maxDepth(...)、self.invertTree(...) 调用。

## 三、中序遍历：把值加入同一个列表

函数含义：dfs(node) 按中序遍历当前子树，把值依次加入 ans。

```python
if node is None:
    return

dfs(node.left)
ans.append(node.val)
dfs(node.right)
```

左子树全部完成后，才能添加当前根节点，再处理右子树。上图结果为：

```python
[4, 2, 1, 3]
```

前、中、后序中的位置，指的是“访问根节点”的位置：

| 遍历方式 | 顺序 |
| --- | --- |
| 前序 | 根、左、右 |
| 中序 | 左、根、右 |
| 后序 | 左、右、根 |

dfs 不负责返回结果列表，结果保存在外层的 ans 中。ans.append(...) 修改同一个列表，不需要 nonlocal。定义 dfs 时不执行函数体，所以只要在 dfs(root) 调用之前创建 ans = [] 即可。

## 四、最大深度：接收数字，再返回数字

函数含义：maxDepth(root) 返回以 root 为根的子树有多少层。

```python
if root is None:
    return 0

l_depth = self.maxDepth(root.left)
r_depth = self.maxDepth(root.right)
return max(l_depth, r_depth) + 1
```

上图的返回过程：

```text
空树：返回 0
节点 4：max(0, 0) + 1 = 1
节点 2：max(1, 0) + 1 = 2
节点 3：max(0, 0) + 1 = 1
节点 1：max(2, 1) + 1 = 3
```

加上的 1 是当前根节点这一层。l_depth、r_depth 是每层各自的局部变量，保存下一层返回的整数。

## 五、翻转二叉树：修改连接，再返回节点

函数含义：invertTree(root) 翻转当前子树，并返回它的根节点。

```python
if root is None:
    return None

left = self.invertTree(root.left)
right = self.invertTree(root.right)
root.left = right
root.right = left
return root
```

left 和 right 是已经翻转的子树根节点引用。通过根节点就可以访问整棵子树，不需要复制所有节点。

```text
翻转前：       翻转后：
    1              1
   / \            / \
  2   3          3   2
 /                    \
4                      4
```

先完成原左右子树的翻转，再交换当前节点的左右连接。返回的 root 仍是同一个根节点对象，但其内部连接已经修改。

## 六、关键疑问：为什么三个边界返回值不同

判断边界返回值，先看上一层需要拿它做什么。

| 函数 | 上一层如何使用返回值 | 空节点时 |
| --- | --- | --- |
| dfs | 不使用返回值，通过 ans 收集结果 | return |
| maxDepth | 用于 max 和加法 | return 0 |
| invertTree | 用作左右孩子的连接 | return None |

Python 中单独的 return 等价于 return None，所以第一种和第三种实际返回值相同，只是函数职责不同。

- 空树没有节点可以加入 ans：直接结束当前 dfs。
- 空树的深度为 0：返回 0，叶子节点才能算出 max(0, 0) + 1。
- 空树翻转后仍然没有根节点：返回 None，供上一层连接。

不能把 maxDepth 的空树返回值改为 None，否则无法正常比较和加 1；也不能把 invertTree 的空树返回值改为 0，否则会把孩子引用错误地设成整数。

## 七、递归的思考顺序与复杂度

1. 明确函数处理哪棵子树，以及返回什么。
2. 明确空树如何处理。
3. 相信左右递归能完成各自的任务。
4. 写出当前节点这一层需要做的事。

这三个算法都处理每个节点一次，时间复杂度为 O(n)。递归栈空间为 O(h)，h 是树的高度；平衡时为 O(log n)，退化成单链时为 O(n)。中序遍历另需 O(n) 存放输出列表。

## 题解来源

前两题参考用户提供的灵茶山艾府题解，代码注释和笔记根据本次学习整理：

- [二叉树的中序遍历](https://leetcode.cn/problems/binary-tree-inorder-traversal/solutions/3844031/tu-jie-morris-bian-li-xian-suo-er-cha-sh-cm2s/)
- [二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/solutions/2010612/kan-wan-zhe-ge-shi-pin-rang-ni-dui-di-gu-44uz/)
