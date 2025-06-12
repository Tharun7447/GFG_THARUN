from heapq import heappush, heappop, nsmallest
class Solution:
    def printKClosest(self, arr, k, x):
        return [-i[1] for i in nsmallest(k,[(abs(x-i) if x!=i else float('inf'),-i) for i in arr])]