# Projectinf user saving based on expenditure

mth_income =  int(input("Enter your monthly income: ") )
mth_expenses =  int(input("Enter your total monthly expenses: "))

# Monthy savings according to user expenses and income
mth_savings = mth_income - mth_expenses  

print(f"Your monthly savings are {mth_savings}.")

# Annual savings of user
projected_savings = mth_savings * 12 + (mth_savings * 12 * 0.05)

print(f"Projected savings after one year, with interest, is: {projected_savings}.")
