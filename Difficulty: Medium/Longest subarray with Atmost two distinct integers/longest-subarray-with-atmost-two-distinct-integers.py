class Solution:
    def totalElements(self, arr):
        l = 0
        ans = 0
        from collections import defaultdict
        dic = defaultdict(int)
        for r in range(len(arr)):
            dic[arr[r]]+=1
            while len(dic)>2:
                dic[arr[l]]-=1
                if dic[arr[l]]==0:
                    del dic[arr[l]]
                l+=1
            if len(dic)<3:
                ans = max(ans,r-l+1)
        return ans