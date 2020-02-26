
import os
import csv 

csv_file = os.path.join("..","PyBank","Budget_Data.csv")

with open (csv_file,'r') as csvfile: 
    csvreader=csv.reader(csvfile,delimiter=',') 

    monthtotal = 0 
    net_total = 0 
    date = []
    PL = []
    total_change = 0 

    header = next(csvreader)

    for row in csv.reader(csv_file):
        date.append(row[0])
        monthtotal = monthtotal + 1  
       

        net_total.append(int(row[1]))
        net_total = net_total + (int(row[1]))

    for x,y in zip(PL,PL[1]):
        PL.append(int(y) - int(x))
        total_change = sum(PL)
        average = total_change/monthtotal

greatest_inc = max(PL)
greatest_dec = min(PL)

print("Financial Analysis")
print("------------------------")
print("Total months: " + str(monthtotal))
print("Total volume: " + str(net_total))
#The average change in "Profit/Losses" between months over the entire period
print("Average monthly change: "+ str(average))
#The greatest increase in profits 
print("Greatest increase: " + str(greatest_inc))
#The greatest decrease in losses 
print("Greatest decrease: " + str(greatest_dec))

##Output to text file
text_file = open("PYBankFinancials.txt", "w")
text_file.write("Financial Analysis\n")
text_file.write("------------------------\n")
text_file.write("Total months: " + str(monthtotal) + "\n")
text_file.write("Total volume: " + str(net_total) + "\n")
text_file.write("Average monthly change: " + str(average) + "\n")
text_file.write("Greatest increase: " + str(greatest_inc) + "\n")
text_file.write("Greatest decrease: " + str(greatest_de) + "\n")
text_file.close()          
        



        



