"""
Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.val=x
        self.next=None

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def is_prime(self, n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def nearest_prime(self, n):
        if n <= 1:
            return 2
        offset = 0
        while True:
            if self.is_prime(n - offset):
                return n - offset
            if self.is_prime(n + offset):
                return n + offset
            offset += 1

    def primeList(self, head):
        curr = head
        while curr:
            curr.val = self.nearest_prime(curr.val)
            curr = curr.next
        return head

        # code here
        



#{ 
 # Driver Code Starts
class Node:

    def __init__(self, x):
        self.val = x
        self.next = None


def printList(node):
    while (node != None):
        print(node.val, end=" ")
        node = node.next
    print()


def inputList():

    val = [int(i) for i in input().strip().split()
           ]  #all data of linked list in a line
    head = Node(val[0])
    tail = head
    for i in range(1, len(val)):
        tail.next = Node(val[i])
        tail = tail.next
    return head


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        head = inputList()

        obj = Solution()
        res = obj.primeList(head)

        printList(res)

        print("~")

# } Driver Code Ends