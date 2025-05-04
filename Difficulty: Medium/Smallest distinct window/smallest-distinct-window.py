from collections import defaultdict

class Solution:
    def findSubString(self, s):
        if not s:
            return 0

        unique_chars = set(s)
        required = len(unique_chars)

        left = 0
        min_len = float('inf')
        char_count = defaultdict(int)
        formed = 0

        for right in range(len(s)):
            char_count[s[right]] += 1
            if char_count[s[right]] == 1:
                formed += 1

            while formed == required:
                min_len = min(min_len, right - left + 1)
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    formed -= 1
                left += 1

        return min_len

    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    T = int(input())
    while (T > 0):
        str = input()
        ob = Solution()
        print(ob.findSubString(str))

        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends