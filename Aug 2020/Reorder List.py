# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return
        curNode = head
        stack = []
        while curNode:
            stack.append(curNode)
            curNode = curNode.next

        cnt, isOdd = divmod(len(stack),2 )

        curNode = head
        tmp = None
        for i in range(cnt):
            tmp = curNode.next
            curNode.next = stack.pop(-1)
            if i != cnt - 1:
                curNode.next.next = tmp
                curNode = tmp
        if isOdd:
            tmp.next = None
            curNode.next.next = tmp
        else:
            curNode.next.next = None
        return head

# head = ListNode(1,
#                 next=ListNode(2,
#                               next=ListNode(3,
#                                             next=ListNode(4,
#                                                           next=ListNode(5,
#                                                                         next=None)))))
head = ListNode(1,
                next=ListNode(2,
                              next=None))
root = Solution().reorderList(head)
while root:
    print(root.val)
    root = root.next
