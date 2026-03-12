def main():
    total_cost = 50
    current_sum = 0
    valid_coins = [5,10,25]


    while current_sum < total_cost:
        amount_due = total_cost-current_sum
        print(f"Amount due: {amount_due}")
        coin = int(input("Insert a coin: "))
        if coin in valid_coins:
            current_sum += coin
    if current_sum >= total_cost:
        print(f"Dispensing a Coke and Change owed: {current_sum - total_cost}")

if __name__ == "__main__":
    main()