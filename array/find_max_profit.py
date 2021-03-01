'''
Given an array of numbers consisting of daily stock prices,
calculate the maximum amount of profit that can be made from buying on one day and selling on another.
'''

''' Solution 1 Brute Force '''
A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def buy_and_sell_once(A):
  max_profit = 0
  for i in range(len(A)-1):
    for j in range(i+1, len(A)):
      if A[j] - A[i] > max_profit:
          max_profit = A[j] - A[i]
  return max_profit

print(buy_and_sell_once(A))

''' Best Solution '''

A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

# Time Complexity: O(n)
# Space Complexity: O(1)
def buy_and_sell_once(prices):
  max_profit = 0.0
  min_price = float('inf')
  for price in prices:
    min_price = min(min_price, price)
    compare_profit = price - min_price
    max_profit = max(max_profit, compare_profit)
  return max_profit

print(buy_and_sell_once(A))

'''
We set max_profit and min_price to 0 and infinity respectively (lines 6-7).
The list prices is iterated using a for loop on line 8.
As we are supposed to keep track of the minimum price,
we update min_price using the min function on line 9 where min_price is the minimum amount between min_price and price
of the current iteration.
In the next line, we store the calculated profit (price - min_price) in compare_profit.
As we also need to keep a check on the max_profit,
we update max_profit to the maximum value between max_profit and compare_profit on line 11.
After we are done with the iteration of prices, we return max_profit on line 12.
'''

