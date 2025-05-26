class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

class Solution:
    def sortedInsert(self, head, data):
        #code here

        n = Node(data)
        n.next = head.next
        head.next = n
        if data < head.data:
            head.data, n.data = n.data, head.data
        else:
            while n.data > n.next.data and n.next != head:
                n.data, n.next.data = n.next.data, n.data
                n = n.next
        return head