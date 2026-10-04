---
title: "Day 13：链表归并排序与 LRU 缓存"
aliases:
  - "Day 13 学习总结"
tags:
  - LeetCode
  - Python
  - 链表
  - 归并排序
  - 哈希表
  - LRU
  - day13
date: 2026-09-29
status: completed
---

# Day 13：链表归并排序与 LRU 缓存

当天完成：

1. [[排序链表_自顶向下归并排序.py|148. 排序链表（自顶向下）]]
2. [[排序链表_自底向上归并排序.py|148. 排序链表（自底向上）]]
3. [[LRU缓存_哈希表加双向链表.py|146. LRU 缓存]]

## 一、排序链表：自顶向下归并

过程是：

```text
寻找中点并断开链表
        ↓
递归排序左半段和右半段
        ↓
合并两条有序链表
```

### `previous.next = None` 必须放在循环外

快慢指针先完整找到中点，再执行：

```python
previous.next = None
```

这句是在 `previous` 与 `slow` 之间切断链表，不是把 `slow` 单独变成一个节点。如果放在循环中，链表会在中点确定前被提前切断。

### `current.next` 与 `current`

合并后拼接剩余链表时，必须写：

```python
current.next = list1 if list1 else list2
```

如果写成：

```python
current = list1 if list1 else list2
```

只是让局部变量 `current` 指向另一个节点，没有修改结果链表中任何节点的 `next`，因此剩余链表不会被接上。

### Python 条件表达式

```python
current.next = list1 if list1 else list2
```

执行时先判断中间的 `list1`：

```python
if list1:
    current.next = list1
else:
    current.next = list2
```

循环结束时至多只有一条链表剩下节点，而这些节点本来就连接在一起，所以只需要接上它的头节点。

- 时间复杂度：`O(n log n)`
- 递归调用栈空间：`O(log n)`

## 二、排序链表：自底向上归并

不使用递归，而是从长度为 `1` 的有序段开始：

```text
step = 1：合并相邻单节点
step = 2：合并相邻长度 2 的有序段
step = 4：合并相邻长度 4 的有序段
step = 8：继续倍增
```

每组使用两次 `splitList`：

```python
head1 = current
head2 = self.splitList(head1, step)
current = self.splitList(head2, step)
```

得到：

```text
head1   → 第一段
head2   → 第二段
current → 尚未处理部分
```

合并函数同时返回头节点和尾节点：

```python
merged_head, merged_tail = self.mergeTwoLists(head1, head2)
```

其中：

```text
merged_head 指向合并后第一个真实节点
merged_tail 指向合并后最后一个真实节点
merged_tail.next 才是 None
```

自底向上归并的优势是没有递归调用栈：

- 时间复杂度：`O(n log n)`
- 额外空间复杂度：`O(1)`

## 三、`self` 与函数调用

`self` 表示当前正在操作的对象。在同一个类中调用实例方法：

```python
self.middleNode(head)
self.sortList(head)
self.mergeTwoLists(head1, head2)
```

例如：

```python
solution.middleNode(head)
```

Python 会自动把 `solution` 传给方法的第一个参数 `self`，可近似理解为：

```python
Solution.middleNode(solution, head)
```

但类外的全局函数直接写：

```python
middleNode(head)
```

其他类的普通方法通过对象调用：

```python
tool.middleNode(head)
```

## 四、146. LRU 缓存

LRU 的规则是：缓存满后，淘汰最长时间没有被使用的数据。

```text
字典：根据 key 在 O(1) 平均时间内找到节点
双向链表：在 O(1) 时间内调整使用顺序
```

链表顺序：

```text
dummy ⇄ 最近使用 ⇄ ... ⇄ 最久未使用 ⇄ dummy
```

### `Node` 与 `ListNode`

普通 `ListNode` 只有 `val` 和 `next`，是单向链表节点。LRU 需要通过 `prev` 和 `next` 在 `O(1)` 时间内删除任意节点，因此使用自定义双向节点 `Node`。

```python
class Node:
    __slots__ = "prev", "next", "key", "value"
```

`__slots__` 限定节点允许的属性，可节省内存，但它不会自动初始化属性。

```python
self.key = key
self.value = value
```

右边是创建节点时传入的参数，左边是真正保存在当前节点对象里的属性。如果固定写成 `self.key = 0`，真实传入的键就会被忽略。

### `self.dummy` 与局部参数

```python
self.dummy = Node()
```

表示将哨兵节点长期保存在当前 `LRUCache` 对象中，各个方法都可以访问它。

```python
def remove(self, node: Node):
```

`node` 是调用方法时传入的局部参数，所以写 `node.prev`，而不是 `self.node.prev`。

### 字典保存的映射

```python
self.key_to_node = {}
```

保存：

```text
key → Node节点对象
```

存入映射：

```python
self.key_to_node[key] = node
```

根据键取出节点：

```python
node = self.key_to_node[key]
```

这不会复制节点，`node` 与字典中的值指向同一个对象。

删除完整键值对要通过键：

```python
del self.key_to_node[back_node.key]
```

给值赋为 `None` 不是删除，因为键仍然存在，字典长度也不会减少。

### 双向链表删除和头插

删除 `node`：

```python
node.prev.next = node.next
node.next.prev = node.prev
```

头插 `node`：

```python
node.prev = self.dummy
node.next = self.dummy.next
self.dummy.next = node
node.next.prev = node
```

超过容量时，`dummy.prev` 是最久未使用的真实节点。必须同时从字典和链表删除：

```python
del self.key_to_node[back_node.key]
self.remove(back_node)
```

- `get` 平均时间复杂度：`O(1)`
- `put` 平均时间复杂度：`O(1)`
- 空间复杂度：`O(capacity)`
