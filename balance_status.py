def balance_status(balance):
    if balance < 0:
       status = "마이너스 잔액"

    elif balance == 0:
        status = "잔액 없음"

    else:
        status = "정상 잔액"

    return status


print(balance_status(50))