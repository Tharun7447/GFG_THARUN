class Solution:
    def sumSubstrings(self,s):
        # code here
        su=0
        
        for i in range(1,len(s)+1):
            k=0
            j=k+i
            while j<len(s)+1:
                su+=int(s[k:j])
                k+=1
                j+=1
        return su