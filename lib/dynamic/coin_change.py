# Coin Change Problem
def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage
coin_set = [1, 2, 5]
amount = 11
print("Minimum number of coins needed:", min_coins(coin_set, amount))
