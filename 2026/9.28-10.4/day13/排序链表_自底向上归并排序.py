from typing import Optional


# 本地学习用节点定义；力扣已经提供 ListNode 时不需要重复提交。
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getListLength(self, head: Optional[ListNode]) -> int:
        """返回链表的节点数量。"""

        length = 0

        while head is not None:
            length += 1
            head = head.next

        return length

    def splitList(
        self,
        head: Optional[ListNode],
        size: int,
    ) -> Optional[ListNode]:
        """保留前 size 个节点并断开，返回剩余链表的头节点。"""

        current = head

        # current 最终应停在这一段的第 size 个节点。
        for _ in range(size - 1):
            if current is None:
                break
            current = current.next

        # 剩余长度不超过 size，已经没有下一段。
        if current is None or current.next is None:
            return None

        next_head = current.next
        current.next = None

        return next_head

    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> tuple[Optional[ListNode], ListNode]:
        """合并两条有序链表，同时返回合并后的头节点和尾节点。"""

        dummy = ListNode()
        current = dummy

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        current.next = list1 if list1 else list2

        # 停止时 current 指向最后一个真实节点，current.next 才是 None。
        while current.next is not None:
            current = current.next

        return dummy.next, current

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """从长度 1 开始，逐轮合并长度为 1、2、4、8... 的有序段。"""

        length = self.getListLength(head)
        dummy = ListNode(0, head)
        step = 1

        while step < length:
            new_list_tail = dummy
            current = dummy.next

            while current is not None:
                # 连续切出两段最长为 step 的链表。
                head1 = current
                head2 = self.splitList(head1, step)
                current = self.splitList(head2, step)

                merged_head, merged_tail = self.mergeTwoLists(head1, head2)

                # 把本组合并结果接到这一轮已完成部分的后面。
                new_list_tail.next = merged_head
                new_list_tail = merged_tail

            step *= 2

        return dummy.next


# 时间复杂度：O(n log n)。
# 额外空间复杂度：O(1)。
