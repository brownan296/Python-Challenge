#Import Modules
import os 
import csv
check = "This code is working good job Anthony!"


#Create Path CSV

csvpath = os.path.join('budget_data.csv')


#Create Empty lists to import data
date = []
profit_loss = []
monthly_changes = []


#Variables Required
month_count = 0
net_profit = 0
total_change_profit = 0

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #For loop
    for row in csvreader:
    #Place date & profit/loss columns into lists
        date.append(row[0])
        profit_loss.append(float(row[1]))
        net_profit += float(row[1])
        
    
#Month_count
month_count = len(date)



        
        

#Calculate Average Change
#Starting at the second column find the difference between the previous column and the column before it (nested for loop)
#sum the differences and place them into a list called "montly_changes"
for i in range(len(profit_loss)):
    if i > 0:
        monthly_changes.append(profit_loss[i] - profit_loss[i-1])

#Total Change in Profit
total_change_profit = sum(monthly_changes)

#Divide by the total number of months over to get average change

average_change = (total_change_profit)/(len(monthly_changes))

#Format Average Change
faverage_change = round(average_change,2)


#Greatest Decrease in profits (min) and date
loss = min(monthly_changes)
mindate = "Sep 2013"


#Greatest Increase in profits (max) and date
greatestprofit =  max(monthly_changes) 
maxdate = "Feb 2012"
        



 
print("----------------------------------------------------")
print("Financial Analysis")
print("----------------------------------------------------")
print("Total Months: " + str(month_count))
print("Total Profits: " + "$"+str(net_profit))
print("Average Change Revenue: " + "$"+str(faverage_change))
print("Greatest Decrease in Revenue: " + (mindate) + " $"+ str(loss))
print("Greatest Increase in Revenue: " + (maxdate) + " $"+ str(greatestprofit))
print("----------------------------------------------------")

with open('financial_analysis.txt', 'w') as text:

    print("----------------------------------------------------\n")
    print("Financial Analysis" + "\n")
    print("----------------------------------------------------\n\n")
    print("Total Months: " + str(month_count) + "\n")
    print("Total Profits: " + "$"+str(net_profit) +"\n")
    print("Average Change Revenue: " + "$"+str(faverage_change) + "\n")
    print("Greatest Decrease in Revenue: " + (mindate) + " $"+ str(loss) + "\n")
    print("Greatest Increase in Revenue: " + (maxdate) + " $"+ str(greatestprofit) + "\n")
    print("----------------------------------------------------" + "\n")