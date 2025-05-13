#User function Template for python3

class Solution:
    def nCr(self, n, r):
        if r > n:
            return 0
        # code here
        def factorial(x):
            if x == 0:
                return 1
            y = 1
            for i in range(1, x+1):
                y = y*i
            return y
        z = factorial(r)*factorial(n-r)
        return int(factorial(n) / z)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        r = int(input())
        ob = Solution()
        print(ob.nCr(n, r))
        print("~")
# } Driver Code Ends