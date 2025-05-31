import heapq

class Solution:
    def kthSmallest(self, matrix, k):
        heap = []
        n = len(matrix)
        for i in range(n):
            heapq.heappush(heap,(matrix[i][0],i,0))
        for ech in range(k-1):
            value,row,col = heapq.heappop(heap)
            if col+1 < n:
                heapq.heappush(heap,(matrix[row][col+1],row,col+1))
        return heap[0][0]