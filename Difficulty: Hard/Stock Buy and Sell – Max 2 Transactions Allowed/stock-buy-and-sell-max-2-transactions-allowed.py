class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n < 2:
            return 0
        profit1, profit2 = 0, 0
        min_price1, min_price2 = float('inf'), float('inf')
        for price in prices:
            min_price1 = min(min_price1, price)
            profit1 = max(profit1, price - min_price1)
            min_price2 = min(min_price2, price - profit1)
            profit2 = max(profit2, price - min_price2)
        return profit2
#{ 
 # Driver Code Starts
#Initial template for Python 3
import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxProfit(arr))
        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends