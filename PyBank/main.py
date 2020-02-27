#import dependencies 
import os
import csv 

bank_csv = os.path.join('budget_data.csv')
#read csv file and define values 
with open(bank_csv, "r") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    date = [] #list for date column 
    #starting values 
    net_total = 0
    months = 0
    pl = [] #list for profit/loss colum
    transactional = [] #list to hold the difference
    #skip header 
    header = next(csvreader)
    #for loop to moves through rows 
    for row in csv.reader(csv_file):
        #append row of list 
        date.append(row[0])
        transactional.append(row[1])
        #calculae total profit/loss
        net_total = net_total + (int(row[1]))
        #calculate months 
        months = months + 1

    #zip so that the profit/loss change can be calculated 
    for x, y in zip(transactional, transactional[1:]):
        #Append to calculate the profit/loss change 
        pl.append(int(y) - int(x))

        total_change = sum(pl)
        average = total_change / months
        average = "{:.2f}".format(average) # formatting average 

#The greatest increase or decrease in profits (date and amount) 
greatest_increase = max(pl) #getting max
monthinc = pl.index(greatest_increase) + 1  # geting index of max 
monthdateinc = date[monthinc] # getting month associated with index of max 
greatest_decrease = min(pl) #getting min 
monthdec = pl.index(greatest_decrease) + 1  #getting index of min 
monthdatedec = date[monthdec] #getting month associated with index of min 

#Print out of results 
print("Financial Analysis")
print("------------------------")
print("Total months: " + str(months))
print("Total volume: $" + str(net_total))
#The average change in "Profit/Losses" between months over the entire period
print("Average monthly change: $"+ str(average))
#The greatest increase in profits (date and amount) over the entire period
print("Greatest increase: $" + str(greatest_increase)  + str(monthdateinc))
#The greatest decrease in losses (date and amount) over the entire period
print("Greatest decrease: $" + str(greatest_decrease)  + str(monthdatedec))

#Output to text file
text_file = open("PYBankResults.txt", "w")
text_file.write("Financial Analysis\n") # \n to signify end of line 
text_file.write("------------------------\n")
text_file.write("Total months: " + str(months) + "\n")
text_file.write("Total volume: $" + str(net_total) + "\n")
text_file.write("Average monthly change: $" + str(average) + "\n")
text_file.write("Greatest increase: " + str(greatest_increase) + "%" + str(monthdateinc) + "\n")
text_file.write("Greatest decrease: " + str(greatest_decrease) + "%" + str(monthdatedec) + "\n")
#close file 
text_file.close() 
