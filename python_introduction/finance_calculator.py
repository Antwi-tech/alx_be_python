# Projectinf user saving based on expenditure

monthly_income =  int(input("Enter your monthly income: ") )
monthly_expenses =  int(input("Enter your total monthly expenses: "))

# Monthy savings according to user expenses and income
monthly_savings = monthly_income - monthly_expenses 

print(f"Your monthly savings are ${monthly_savings:.2f}.")

# Annual savings of user
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
