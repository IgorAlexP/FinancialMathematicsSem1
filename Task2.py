# Входные данные
target_value = 350000  # Целевая стоимость к пенсии
annual_interest_rate = 0.08  # Годовая ставка доходности (8%)
years_until_retirement = 30  # Количество лет до пенсии

# Рассчитываем годовой вклад (сумму, которую нужно инвестировать каждый год)
annual_investment = target_value / ((1 + annual_interest_rate) ** years_until_retirement - 1) / annual_interest_rate

# Выводим результат
print(f"Инвестор должен инвестировать каждый год: ${annual_investment:.2f}")
