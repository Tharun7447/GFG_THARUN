#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        transformed = [1 if x > k else -1 for x in arr]
        prefix_sum = 0
        max_len = 0
        first_occurrence = {}

        for i in range(n):
            prefix_sum += transformed[i]
            if prefix_sum > 0:
                max_len = i + 1
            if prefix_sum not in first_occurrence:
                first_occurrence[prefix_sum] = i
            if (prefix_sum - 1) in first_occurrence:
                length = i - first_occurrence[prefix_sum - 1]
                max_len = max(max_len, length)

        return max_len


#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        
        arr = [int(x) for x in input().strip().split()]
        k = int(input())
        
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        print("~")
        t -= 1
# } Driver Code Ends