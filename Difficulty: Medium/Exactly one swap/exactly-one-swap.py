class Solution:
    def countStrings(self, s): 
        #code here
        a=[0]*26 
        # a={}
        s1=0
        for i in s:
            a[ord(i)-ord('a')]+=1
            if a[ord(i)-ord('a')]>1:
                s1=1 
        # s=1
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                    s1+=a[i]*a[j]
            # print(s)
        return s1