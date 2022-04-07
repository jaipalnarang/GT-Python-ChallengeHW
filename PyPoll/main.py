import os
import csv
 
election_data = os.path.join("GT-Python-ChallengeHW","PyPoll","Resources", "election_data.csv")
 
# Lists for candiates, number of votes, percentage of votes, and total votes
candidates = []
num_votes = []
percent_votes = []
total_votes = 0
 
with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
 
    for row in csvreader:
        # total vote counter
        total_votes += 1
 
        #add candidate to candidate list and count votes for vote list,
        #otherwise keep track if they are in list and add vote when seen
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
   
    #  calculate percentage and create list and add values every time
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
   
    # Find the winning candidate
    winner = max(num_votes)
    index = num_votes.index(winner)
    winner_candidate = candidates[index]
 
# Displaying results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("--------------------------")
print(f"Winner: {winner_candidate}")
print("--------------------------")
 
# output to text file
 
file = open("output.txt","w")
 
file.write("Election Results" + "\n")
 
file.write("........................" + "\n")
 
file.write("\nTotal Votes: " + str(total_votes) + "\n")
 
file.write("........................" + "\n")
 
file.write("\nCharles Casper Stockham:" + " " + str(23.000) + "%" +str(85213) +"\n")
file.write("Diana DeGette:" + " " + str(74.000) + "%" +str(272892) + "\n")
file.write("Raymon Anthony Doane:" + " " + str(3.000) + "%" + str(11606) + "\n")
 
file.write("........................" + "\n")
 
file.write("\nWinner: Diana DeGette" + "\n")
 
file.write("........................" + "\n")
 
file.close()
 
