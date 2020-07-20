# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        while head and head.val == val:
            head = head.next

        if not head: return head
        curNode = head.next
        preNode = head

        while curNode:
            if curNode.val == val:
                preNode.next = curNode.next
                curNode = curNode.next
            else:
                preNode = curNode
                curNode = curNode.next
        return head

head = ListNode(1,
                ListNode(2,
                         ListNode(6,
                                  ListNode(3,
                                           ListNode(4,
                                                    ListNode(5,
                                                             ListNode(6)))))))
res = Solution().removeElements(head, 6)

while res:
    print(res.val)
    res = res.next


