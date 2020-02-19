#!/usr/bin/python3

import argparse


def find_max_profit(prices):
    max_profit = 0
    buy_price = 0
    sell_price = 0
    change_buy_price = True
    is_sorted = all(prices[i] >= prices[i + 1] for i in range(len(prices) - 1))
    if is_sorted:
        return prices[1] - prices[0]
    for i in range(len(prices) - 1):
        sell_price = prices[i + 1]
        if change_buy_price:
            buy_price = prices[i]
        if sell_price < buy_price:
            change_buy_price = True
            continue
        else:
            profit = sell_price - buy_price
            print(profit)
            if profit > max_profit:
                max_profit = profit
                change_buy_price = False

    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument(
        'integers',
        metavar='N',
        type=int,
        nargs='+',
        help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
