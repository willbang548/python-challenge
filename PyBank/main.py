import os
import pandas as pd
 

path_to_file = os.path.join("Resources","budget_data.csv")
bank_budget = pd.read_csv(path_to_file)

#The total number of months included in the dataset
month_num = bank_budget.shape[0]

#The net total amount of "Profit/Losses" over the entire period
total = bank_budget['Profit/Losses'].sum()

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
bank_budget['Profit/Losses Change'] = bank_budget['Profit/Losses'] - bank_budget['Profit/Losses'].shift(1)
avg_change = bank_budget['Profit/Losses Change'].mean()

#The greatest increase in profits (date and amount) over the entire period
max_change = bank_budget['Profit/Losses Change'].max()
max_date = bank_budget.loc[bank_budget['Profit/Losses Change'].idxmax(), 'Date']

#The greatest decrease in profits (date and amount) over the entire period
min_change = bank_budget['Profit/Losses Change'].min()
min_date = bank_budget.loc[bank_budget['Profit/Losses Change'].idxmin(), 'Date']

result = f"""Financial Analysis
----------------------------
Total Months: {month_num}
Total: ${total:.0f}
Average Change: ${avg_change:.2f}
Greatest Increase in Profits: {max_date} (${max_change:.0f})
Greatest Decrease in Profits: {min_date} (${max_change:.0f})
"""

print(result)

with open("analysis/results.text", "w") as file:
    file.write(result)