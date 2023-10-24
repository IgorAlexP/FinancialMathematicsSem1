cash_flows = [2000, 5000, 10000]  # Денежные потоки в каждом из трех лет
risk_free_rate = 0.01  # Безрисковая ставка (1%)
inflation_rate = 0.06  # Ожидаемая инфляция (6%)
risk_premium = 0.04  # Премия за риск (4%)

# Рассчитываем ставку дисконтирования
discount_rate = risk_free_rate + inflation_rate + risk_premium

# Рассчитываем приведенную стоимость (NPV)
npv = sum([cf / (1 + discount_rate) ** (i + 1) for i, cf in enumerate(cash_flows)])

# Выводим результат
print(f"Приведенная стоимость потоков по проекту: ${npv:.2f}")
