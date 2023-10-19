money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05
count_month = 0

difference = spend - salary

while money_capital > difference:
    money_capital -= difference
    spend *= 1 + increase
    difference = spend - salary
    count_month += 1

print("Количество месяцев, которое можно протянуть без долгов:", count_month)
