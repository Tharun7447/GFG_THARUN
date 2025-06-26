from collections import Counter
class Solution:
    def minValue(self, s, k):
        freq = Counter(s)
        freq_values = list(freq.values())
        
        if len(freq_values)==1:
            return freq_values[0]*freq_values[0]
            
        freq_values.sort()
        
        while k>0:
            freq_values[-1]-=1
            freq_values.sort()
            k-=1
        sum1=0    
        for i in range(len(freq_values)):
            sum1+=freq_values[i]*freq_values[i]
        return sum1