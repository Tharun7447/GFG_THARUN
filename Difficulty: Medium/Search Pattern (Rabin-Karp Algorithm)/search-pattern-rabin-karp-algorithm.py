class Solution:
    def search(self, pat, txt):
        n, m, j = len(txt), len(pat), 0
        d, q = 256, 101  
        h = pow(d, m-1) % q  
        p, t = 0, 0  
        
        for i in range(m):
            p = (d * p + ord(pat[i])) % q
            t = (d * t + ord(txt[i])) % q
        
        res = []
        for i in range(n - m + 1):
            if p == t:
                if pat == txt[i:i+m]:
                    res.append(i + 1)  
            if i < n - m:
                t = (d * (t - ord(txt[i]) * h) + ord(txt[i+m])) % q
                if t < 0: t += q
        
        return res