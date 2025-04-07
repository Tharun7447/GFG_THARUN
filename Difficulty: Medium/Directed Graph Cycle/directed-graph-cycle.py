
class Solution:
    def isCycle(self, V, edges):
        graph = [[] for _ in range(V)]
        for u, v in edges:
            graph[u].append(v)

        visited = [0] * V  # 0: unvisited, 1: visiting, 2: visited

        def dfs(u):
            if visited[u] == 1:
                return True
            if visited[u] == 2:
                return False
            visited[u] = 1
            for v in graph[u]:
                if dfs(v):
                    return True
            visited[u] = 2
            return False

        return any(dfs(i) for i in range(V))


#{ 
 # Driver Code Starts
from collections import deque


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append((u, v))

        obj = Solution()
        ans = obj.isCycle(V, edges)
        print("true" if ans else "false")


if __name__ == "__main__":
    main()

# } Driver Code Ends