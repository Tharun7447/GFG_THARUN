class Solution:
    def findDuplicate(self, arr):
        seen = set()
        for num in arr:
            if num in seen:
                return num
            seen.add(num)


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        print(ob.findDuplicate(arr))
        print("~")

# } Driver Code Ends