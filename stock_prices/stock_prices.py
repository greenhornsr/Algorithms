#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # declare variables
  current_diff = 0
  profit = prices[1] - prices[0]
  # LOOP THROUGH
  for i in range(len(prices)): # 0 | 1
    print("profit: ", profit)
    # Store i
    current_num = prices[i] # prices[0] > 10
    # LOOP THROUGH THE REST,
    for j in range(i+1, len(prices)): # 0 + 1 > 1 | 2 | 3
        # calculate difference
      current_diff = prices[j] - current_num
      #   check if current diff is > profit
      if current_diff > profit:
        #     set profit 
        profit = current_diff
  return profit  


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))