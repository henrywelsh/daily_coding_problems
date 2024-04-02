# Given a array of numbers representing the stock prices of a company in chronological order,
# write a function that calculates the maximum profit you could have made from buying and selling that stock once.
# You must buy before you can sell it.
#
# For example, given [9, 11, 8, 5, 7, 10], you should return 5,
# since you could buy the stock at 5 dollars and sell it at 10 dollars.


def find_max_profit(all_prices):
    min_value = all_prices[0]
    curr_max_profit = 0
    for price in all_prices:
        if price - min_value > curr_max_profit:
            curr_max_profit = price - min_value
        if price < min_value:
            min_value = price
    return curr_max_profit

if __name__ == "__main__":
    prices = [9, 11, 8, 5, 7, 10]
    print(find_max_profit(prices))
