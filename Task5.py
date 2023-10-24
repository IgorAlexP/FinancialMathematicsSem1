principal = 1000  # Начальная сумма в долларах
annual_interest_rate_1 = 0.11  # Годовая процентная ставка для первого варианта (11%)
annual_interest_rate_2 = 0.115  # Годовая процентная ставка для второго варианта (11.5%)
years = 5  # Количество лет

# Первый вариант: ежемесячная капитализация
compounding_frequency_1 = 12  # Количество раз в год, когда проценты капитализируются

# Второй вариант: ежегодная капитализация
compounding_frequency_2 = 1

# Рассчитываем будущую стоимость для обоих вариантов
future_value_1 = principal * (1 + (annual_interest_rate_1 / compounding_frequency_1))**(compounding_frequency_1 * years)
future_value_2 = principal * (1 + (annual_interest_rate_2 / compounding_frequency_2))**(compounding_frequency_2 * years)

# Сравниваем результаты
if future_value_1 > future_value_2:
    print("Выгодней положить деньги на депозит под 11% с ежемесячной капитализацией.")
elif future_value_2 > future_value_1:
    print("Выгодней положить деньги на депозит под 11.5% с ежегодной капитализацией процентов.")
else:
    print("Оба варианта равноценны.")
