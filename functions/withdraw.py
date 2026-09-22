def withdraw(balance, amount):
    total_amount=balance-amount
    if balance<amount:
        return "출금이 불가능합니다."
    return total_amount

