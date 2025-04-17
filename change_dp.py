def change(amount):
    # print(amount)
    coins = [1,3,4]
    min_coins_result_array = [x for x in range(amount + 1)]
    for money_looper in range(1, amount + 1):
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
if __name__ == '__main__':
    m = int(input())
    print(change(m))