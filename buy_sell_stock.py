def maxProfit(prices):
        b_price= prices[0]
        profit=0
        for i in range(1, len(prices)):
            s_price=prices[i]
            if s_price>b_price:
                profit=max(profit, (s_price-b_price))
            if b_price>s_price:
                b_price = prices[i]
        return profit
    
prices = [7,1,5,3,6,4]
print(maxProfit(prices))