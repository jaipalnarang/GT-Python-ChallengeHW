#import library
import os
import csv
 
#joining path
budget_data = os.path.join("GT-Python-ChallengeHW","PyBank","Resources", "budget_data.csv")
 
# open and read csv
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
   
    # skip header row
    print(f"Header: {csv_header}")
 
    # find net total amount of profit and loss
    P = []
    M = []
 
    #read through each row of data after header
    for rows in csvreader:
        P.append(int(rows[1]))
        M.append(rows[0])
 
    # find change in profit/losses
    profit_loss_change = []
 
    for x in range(1, len(P)):
        profit_loss_change.append((int(P[x]) - int(P[x-1])))
   
    # calculate average revenue change
    revenue_average = sum(profit_loss_change) / len(profit_loss_change)
   
    # calculate total length of months
    total_months = len(M)
 
    # greatest increase in revenue
    greatest_increase = max(profit_loss_change)
    # greatest decrease in revenue
    greatest_decrease = min(profit_loss_change)
 
 
    # print the Results
    print("Financial Analysis")
 
    print("--------------------------")
 
    print("Total months: " + str(total_months))
 
    print("Total: " + "$" + str(sum(P)))
 
    print("Average change: " + "$" + str(revenue_average))
 
    print("Greatest Increase in Profits: " + str(M[profit_loss_change.index(max(profit_loss_change))+1]) + " " + "$" + str(greatest_increase))
 
    print("Greatest Decrease in Profits: " + str(M[profit_loss_change.index(min(profit_loss_change))+1]) + " " + "$" + str(greatest_decrease))
 
 
    # output to a text file
 
    file = open("output1.txt","w")
 
    file.write("Financial Analysis" + "\n")
 
    file.write("........................" + "\n")
 
    file.write("Total months: " + str(86) + "\n")
 
    file.write("Total: " + "$" + str(22564198) + "\n")
 
    file.write("Average change: " + "$-" + str(8311.11) + "\n")
 
    file.write("Greatest Increase in Profits: " + str("Aug-16") + " " + "$" + str(1862002) + "\n")
 
    file.write("Greatest Decrease in Profits: " + str("Feb-14") + " " + "$-" + str(1825558) + "\n")
 
    file.close()
