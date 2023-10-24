# Входные данные
initial_value = 10  # Начальная стоимость (цена покупки) в долларах
ending_value = 50   # Конечная стоимость (цена продажи) в долларах
investment_duration = 6  # Количество лет инвестирования

# Рассчитываем годовую доходность (CAGR)
cagr = ((ending_value / initial_value) ** (1 / investment_duration)) - 1

# Преобразуем в проценты
cagr_percent = cagr * 100

# Выводим результат
print(f"Годовая доходность: {cagr_percent:.2f}%")
