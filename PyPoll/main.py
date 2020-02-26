#import dependencies 
import os 
import csv 

#data path 
poll_csv = os.path.join('election_data.csv')
#read csv file and define values 
with open(poll_csv, "r") as csv_file:
        csvreader = csv.reader(csv_file, delimiter=',')
        line = next(csvreader,None) #skip first line 
        votes = 0 
        vote_count = [] #list for vote count
        candidates = [] # list for candidates 
        #establish loop 
        for line in csvreader:  
            #calculate total votes cast  
            votes = votes +1
            #establish candidate
            candidate = line[2]
            #adding votes to a candidate 
            if candidate in candidates:
                candidate_index = candidates.index(candidate)
                vote_count[candidate_index] = vote_count[candidate_index] + 1
            #new spot for next candidate
            else:
                candidates.append(candidate)
                vote_count.append(1) 
        #variables fot the next calculations 
        percentages = []
        max_votes = vote_count[0]
        max_index = 0 
        
        #percentage of votes 
        for count in range(len(candidates)):
            vote_percent = vote_count[count]/votes*100
            vote_percent = "{:.3f}".format(vote_percent) 
            percentages.append(vote_percent)
            

            if vote_count[count] > max_votes:
                max_votes = vote_count[count]
                max_index = count
            #establish winner 
            winner = candidates[max_index]

            

#print out of results 
print("Election Results")
print("--------------------------")
print(f"Total Votes: {votes}")
print("--------------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_count[count]})")
print("--------------------------")
print(f"Winner:  {winner}")
print("--------------------------")

    
# Write results to export text file
text_file = open("PYPollResults.txt", "w")
text_file.write("Election Results\n") #\n signifies end of line 
text_file.write("-----------------------------\n")
text_file.write(f"Total Votes:  {votes}\n")
text_file.write("-----------------------------\n")
for count in range(len(candidates)):
    text_file.write(f"{candidates[count]}: {percentages[count]}% ({vote_count[count]})\n")
text_file.write("-----------------------------\n")
text_file.write(f"Winner:  {winner}\n")
text_file.write("-----------------------------\n")
    
# Close the text file
text_file.close()

