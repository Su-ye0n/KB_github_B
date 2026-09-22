#feat 수수료 계산_도윤

def calculate_fee(amount, fee_rate):
    fee=round(amount*fee_rate)
    return fee

amount=100000
fee_rate=0.01

print(calculate_fee(amount,fee_rate))


