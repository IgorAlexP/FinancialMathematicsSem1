# Входные данные
loan_amount = 8000000  # Сумма кредита в рублях
annual_interest_rate = 0.10  # Годовая процентная ставка (10%)
loan_term_years = 20  # Срок кредита в годах

# Рассчитываем месячную процентную ставку
monthly_interest_rate = annual_interest_rate / 12

# Рассчитываем общее количество платежей
total_payments = loan_term_years * 12

# Рассчитываем аннуитетный платеж
annuity_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / ((1 + monthly_interest_rate) ** total_payments - 1)

# Рассчитываем общую переплату (сумму процентов)
total_interest_paid = (annuity_payment * total_payments) - loan_amount

# Выводим результат
print(f"Общая переплата по кредиту составит: {total_interest_paid:.2f} рублей")
