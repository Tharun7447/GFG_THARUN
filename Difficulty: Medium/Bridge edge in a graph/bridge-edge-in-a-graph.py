class Solution:
    def isBridge(self, V, edges, c, d):
        from collections import defaultdict
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        time = [0]
        low = [0] * V
        disc = [-1] * V
        res = [False]

        def dfs(u, parent):
            disc[u] = low[u] = time[0]
            time[0] += 1
            for v in graph[u]:
                if v == parent:
                    continue
                if disc[v] == -1:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        if (u == c and v == d) or (u == d and v == c):
                            res[0] = True
                else:
                    low[u] = min(low[u], disc[v])

        for i in range(V):
            if disc[i] == -1:
                dfs(i, -1)
        return res[0]


#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**7)
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        V = int(input())
        E = int(input())
        adj = [[] for _ in range(V)]
        edges = []

        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
            edges.append([u, v])

        c = int(input())
        d = int(input())

        obj = Solution()
        l = obj.isBridge(V, edges, c, d)

        if l:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends