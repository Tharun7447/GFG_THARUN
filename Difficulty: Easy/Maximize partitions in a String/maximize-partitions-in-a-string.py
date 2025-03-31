class Solution:
    def maxPartitions(self, s):
        last_index = {ch: i for i, ch in enumerate(s)}
        count, end = 0, 0

        for i, ch in enumerate(s):
            end = max(end, last_index[ch])
            if i == end:
                count += 1

        return count

        # code here

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input())

    for _ in range(tc):
        s = input()
        obj = Solution()
        print(obj.maxPartitions(s))
        print("~")

# } Driver Code Ends