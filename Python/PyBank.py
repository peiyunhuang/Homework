import os
import csv

def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total/length

PyBankcsv = os.path.join("Resources","budget_data.csv")

profit = []
monthly_changes = []
date = []


with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader :
        date.append(row[0])
        profit.append(int(row[1]))

print()

Total_profit = sum(profit)

for i in range(len(profit)-1):
    monthly_changes.append((profit[i+1]-profit[i]))

average_changes= average(monthly_changes)
print(average_changes)

Max_profits_change=max(monthly_changes)
Min_profits_change=min(monthly_changes)

for i in range(len(monthly_changes)):
    if monthly_changes[i] == Max_profits_change:
        Date_of_Max = date[i+1]
    if monthly_changes[i] == Min_profits_change:
        Date_of_Min = date[i+1]

Total_months = len(date)

print ("Financial Analysis")
print ("Total Months:"+ str(Total_months))
print ("Total"+ str(Total_profit))
print ("Greatest Increase in Profits:"+ Date_of_Max + " ("  + str(Max_profits_change)+")")
print ("Greatest Decrease in Profits:"+ Date_of_Min + " (" + str(Min_profits_change)+")")


output_file = os.path.join ("Resources","budget_data_revised.csv")

with open (output_file, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("Total Months:"+ str(Total_months)+"\n")
    txtfile.write("Total"+ str(Total_profit)+"\n")
    txtfile.write("Greatest Increase in Profits:"+ Date_of_Max + " ("  + str(Max_profits_change)+")"+"\n")
    txtfile.write("Greatest Decrease in Profits:"+ Date_of_Min + " (" + str(Min_profits_change)+")"+"\n")








