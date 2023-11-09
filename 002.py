# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# l1
# ListNode{val: 2, next: ListNode{val: 4, next: ListNode{val: 3, next: None}}}
## check the definition of ListNode before starting

## https://leetcode.com/problems/add-two-numbers/
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def getNextNode(node):
            if node is not None and node.next is not None:
                return node.next
            else:
                return None


        def createNextNode(nod1, nod2, carried = 0):
            if nod1 is None and nod2 is None:
                if carried == 0:
                    return
                return ListNode(val=carried, next=None)

            val = 0
            if nod1 !=None and nod1.val != None:
                val += nod1.val
            if nod2 !=None and nod2.val != None:
                val += nod2.val

            val += carried

            newCarried = 0
            if val >= 10:
                newCarried = 1
                val -= 10

            return ListNode(val=val, next=createNextNode(getNextNode(nod1), getNextNode(nod2), carried=newCarried))

        return createNextNode(l1, l2)

