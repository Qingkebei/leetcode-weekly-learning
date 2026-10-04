from typing import Optional


# 本地学习用节点定义；力扣已经提供 ListNode 时不需要重复提交。
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        """将链表切成左右两段，返回右半段的头节点。"""

        slow = head
        fast = head
        previous = None

        while fast is not None and fast.next is not None:
            previous = slow
            slow = slow.next
            fast = fast.next.next

        # sortList 只会在至少有两个节点时调用 middleNode。
        # previous.next = None 把左右两段真正断开。
        previous.next = None

        return slow

    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> Optional[ListNode]:
        """合并两条已经有序的链表。"""

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

        # 注意是 current.next，只改 current 不会建立链表连接。
        current.next = list1 if list1 else list2

        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """递归切分链表，再在归来时合并有序链表。"""

        if head is None or head.next is None:
            return head

        head2 = self.middleNode(head)

        head1 = self.sortList(head)
        head2 = self.sortList(head2)

        return self.mergeTwoLists(head1, head2)


# 时间复杂度：O(n log n)。
# 递归调用栈空间：O(log n)。
