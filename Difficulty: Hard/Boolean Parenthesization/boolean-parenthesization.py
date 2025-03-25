class Solution:
    def countWays(self, s):
        n = len(s)
        dp_true = [[0] * n for _ in range(n)]
        dp_false = [[0] * n for _ in range(n)]
        
        for i in range(0, n, 2):
            dp_true[i][i] = 1 if s[i] == 'T' else 0
            dp_false[i][i] = 1 if s[i] == 'F' else 0
        
        for length in range(3, n + 1, 2):
            for i in range(0, n - length + 1, 2):
                j = i + length - 1
                dp_true[i][j], dp_false[i][j] = 0, 0
                for k in range(i + 1, j, 2):
                    lt, lf = dp_true[i][k - 1], dp_false[i][k - 1]
                    rt, rf = dp_true[k + 1][j], dp_false[k + 1][j]
                    if s[k] == '&':
                        dp_true[i][j] += lt * rt
                        dp_false[i][j] += lt * rf + lf * rt + lf * rf
                    elif s[k] == '|':
                        dp_true[i][j] += lt * rt + lt * rf + lf * rt
                        dp_false[i][j] += lf * rf
                    elif s[k] == '^':
                        dp_true[i][j] += lt * rf + lf * rt
                        dp_false[i][j] += lt * rt + lf * rf
        
        return dp_true[0][n - 1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input().strip()
        print(Solution().countWays(s))
        print("~")

# } Driver Code Ends