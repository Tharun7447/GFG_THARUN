#User function Template for python3
class Solution:
    def multiplyStrings(self, s1, s2):
        neg = False
        if s1[0] == '-':
            neg = not neg
            s1 = s1[1:]
        if s2[0] == '-':
            neg = not neg
            s2 = s2[1:]
        
        s1 = s1.lstrip('0')
        s2 = s2.lstrip('0')
        
        if not s1 or not s2:
            return '0'
        
        n, m = len(s1), len(s2)
        res = [0] * (n + m)
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                mul = (ord(s1[i]) - ord('0')) * (ord(s2[j]) - ord('0'))
                pos1 = i + j
                pos2 = i + j + 1
                sum_ = mul + res[pos2]
                res[pos1] += sum_ // 10
                res[pos2] = sum_ % 10
        
        result = ''.join(map(str, res)).lstrip('0')
        if neg:
            result = '-' + result
        return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a = input()
        b = input()
        print(Solution().multiplyStrings(a.strip(), b.strip()))

        print("~")

# } Driver Code Ends