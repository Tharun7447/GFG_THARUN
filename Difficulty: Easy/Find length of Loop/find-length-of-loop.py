#User function Template for python3

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def countNodesInLoop(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return self.countLoopLength(slow)
        
        return 0

    def countLoopLength(self, node):
        count = 1
        temp = node.next
        while temp != node:
            count += 1
            temp = temp.next
        return count



#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(node):
    while node:
        print(node.data, end=' ')
        node = node.next
    print()


def loop_here(head, pos):
    if pos == 0:
        return

    walk = head
    for _ in range(1, pos):
        walk = walk.next

    tail = head
    while tail.next:
        tail = tail.next

    tail.next = walk


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split('\n')
    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        k = int(data[index + 1])
        head = Node(arr[0])
        tail = head
        for value in arr[1:]:
            tail.next = Node(value)
            tail = tail.next
        loop_here(head, k)
        ob = Solution()
        res = ob.countNodesInLoop(head)
        print(res)
        print("~")
        index += 2

# } Driver Code Ends