from functions.deposit import deposit
from functions.can_withdraw import can_withdraw
from functions.withdraw import withdraw



print(f"입금 후 잔액: {deposit(100000,50000)}" )
print(f"출금이 가능한가요? - {can_withdraw(150000,120000)}")
print(f"출금 후 잔액: {withdraw(150000,120000)}")