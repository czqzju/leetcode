
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        curNode = head
        while curNode and (curNode.next or curNode.child):
            if curNode.child:
                childHead = self.flatten(curNode.child)
                curNode.child = None
                nextNode = curNode.next
                curNode.next = childHead
                childHead.prev = curNode
                while childHead.next:
                    childHead = childHead.next
                childHead.next = nextNode
                if nextNode:
                    nextNode.prev = childHead
            else:
                curNode = curNode.next

        return head

n1 = Node(1, None, None, None)
n2 = Node(2, n1, None, None)
n1.next = n2
n3 = Node(3, n2, None, None)
n2.next = n3
n4 = Node(4, n3, None, None)
n3.next = n4
n5 = Node(5, n4, None, None)
n4.next = n5
n6 = Node(6, n5, None, None)
n5.next = n6


n7 = Node(7, None, None, None)
n3.child = n7
n8 = Node(8, n7, None, None)
n7.next = n8
n9 = Node(9, n8, None, None)
n8.next = n9
n10 = Node(10, n9, None, None)
n9.next = n10

n11 = Node(11, None, None, None)
n8.child = n11
n12 = Node(12, n11, None, None)
n11.next = n12

x = Solution().flatten(n1)
res = []
while(x):
    res.append(x.val)
    x = x.next

print(res)