def money_change_dynamic(min_coins_result_array, amount, coins):
    for money_looper in range(1, amount+1) :
        for coin_looper in coins:
            # print(coin_looper)
            if money_looper >= coin_looper and min_coins_result_array[money_looper - coin_looper] != (amount + 1):
                # num_coins = money_change_dynamic(min_coins_result_array, money_looper - coin_looper, coins) + 1
                num_coins = min_coins_result_array[money_looper - coin_looper] + 1
                if num_coins < min_coins_result_array[money_looper]:
                    min_coins_result_array[money_looper] = num_coins
                # print(amount, money_looper, num_coins)
    # print(min_coins_result_array)
    # print(min_coins_result_array)
    return min_coins_result_array[amount]

def money_change_greedy(amount, coins):
    sorted_coins = sorted(coins, reverse = True)
    coins_required = [0] * len(coins)
    coin_looper = 0
    while amount > 0 and coin_looper < len(coins):
        current_coin = coins[coin_looper]
        print(amount, current_coin)
        if amount >= current_coin:
            coins_required[coin_looper] = amount//current_coin
            amount = amount % current_coin
        coin_looper += 1
    if amount != 0:
        return -1
    return coins_required
if __name__ == "__main__":
    # print(money_change_greedy(100, [55, 25, 3, 2]))
    amount = 100
    abc = [amount+1]*(amount+1) #[x for x in range(amount + 1)]
    abc[0] = 0
    print(money_change_dynamic(abc, amount, sorted([8, 5, 2], reverse = True)))