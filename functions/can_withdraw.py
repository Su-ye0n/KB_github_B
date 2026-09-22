def can_withdraw(balance, amount):
    if balance < amount:
        return False
    else:
        return True
# print(can_withdraw(balance,amount))
# 예)
# can_withdraw(100000, 120000)
# → False

# can_withdraw(100000, 50000)
# → True