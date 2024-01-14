salary = 5000
spend = 6000
months = 10
increase = 0.03
money_capital = 0

for _ in range(months):
    money_capital += spend - salary
    spend *= 1 + increase

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {round(money_capital)}")
