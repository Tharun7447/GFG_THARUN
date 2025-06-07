class Solution:
    def longestCommonSum(self, a1, a2):
        pfs={0:-1}
        sm=ret=0
        for ix in range(len(a1)):
            sm+=a1[ix]-a2[ix]
            if sm in pfs:
                ret=max(ret,ix-pfs[sm])
            else:
                pfs[sm]=ix
        return ret