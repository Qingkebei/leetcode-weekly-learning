from typing import Optional


class Node:
    """LRU 使用的双向链表节点。"""

    __slots__ = "prev", "next", "key", "value"

    def __init__(self, key=0, value=0):
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None
        self.key = key
        self.value = value


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

        # 哨兵节点构成循环双向链表。
        self.dummy = Node()
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy

        # 字典保存 key -> Node 的映射。
        self.key_to_node: dict[int, Node] = {}

    def get_node(self, key: int) -> Optional[Node]:
        """获取 key 对应的节点，并将其移到链表头部。"""

        if key not in self.key_to_node:
            return None

        node = self.key_to_node[key]
        self.remove(node)
        self.push_front(node)

        return node

    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.value if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)

        if node is not None:
            node.value = value
            return

        node = Node(key, value)

        # 是在字典中增加 key -> node 映射，不是用 node 替换整个字典。
        self.key_to_node[key] = node
        self.push_front(node)

        if len(self.key_to_node) > self.capacity:
            # dummy.prev 是最久没有使用的真实节点。
            back_node = self.dummy.prev

            # 同时从字典和双向链表中删除。
            del self.key_to_node[back_node.key]
            self.remove(back_node)

    def remove(self, node: Node) -> None:
        """将 node 从双向链表的当前位置取出。"""

        node.prev.next = node.next
        node.next.prev = node.prev

    def push_front(self, node: Node) -> None:
        """把 node 插入哨兵节点后面，表示它刚刚被使用。"""

        node.prev = self.dummy
        node.next = self.dummy.next

        self.dummy.next = node
        node.next.prev = node


# get 和 put 的平均时间复杂度：O(1)。
# 空间复杂度：O(capacity)。
