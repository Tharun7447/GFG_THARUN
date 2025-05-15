
from collections import Counter
class Solution:
	def countSubstring(self, s):
		# code here
		freq = Counter(s)
        cnt = 0
        for ch in freq:
            f = freq[ch]
            cnt += (f * (f - 1)) // 2  # pairs (i < j) where s[i] == s[j]
            cnt += f  # each single character
        return cnt


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.countSubstring(s)

        print(answer)
        print("~")

# } Driver Code Ends