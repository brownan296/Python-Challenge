import os
import csv
x = ("This code works....God job Anthony !")

#Set Path for CSV 
election_data = os.path.join("election_data.csv" )

#Create Lists & initialize variables
vote_count = 0
candidates = []
khan_votes = 0
li_votes = 0
otooley_votes = 0
correy_votes = 0


#Open CSV using path
with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)

    #For Loop
    for row in csvreader:
        #Vote Count
         candidates.append(row[2])
         vote_count = len(candidates)


#Votes each candidate receieved
khan_votes = candidates.count('Khan')
otooley_votes = candidates.count("O'Tooley")
li_votes = candidates.count('Li')
correy_votes = candidates.count('Correy')

#Winner
winner = "Khan"
       
#Percentages
khan_perc = (khan_votes) / (vote_count) * 1
otooley_perc = (otooley_votes) / (vote_count) * 1
li_perc = (li_votes) / (vote_count) * 1
correy_perc = (correy_votes)/ (vote_count) * 1
 
#Formatted Percentages
fkhan = format(khan_perc, ".2%")
fotooley = format(otooley_perc, ".2%")
fli = format(li_perc,".2%")
fcorrey = format(correy_perc, ".2%")


print("Election Results")
print("----------------------")
print("Total Votes: " + str(vote_count))
print("----------------------")
print("Khan: " + (fkhan) + " " + str(khan_votes))
print("Correy: " + (fcorrey) + " " +  str(correy_votes))
print("Li: " + (fli) + " " +  str(li_votes))
print("O'Tooley: " + (fotooley) + " " +  str(otooley_votes))
print("----------------------")
print("Winner: " + str(winner))
print("----------------------")

with open('election_results.txt', 'w') as text:
    print("Election Results" + "\n")
    print("----------------------" + "\n")
    print("Total Votes: " + str(vote_count) + "\n")
    print("----------------------" + "\n")
    print("Khan: " + (fkhan) + " " + str(khan_votes) + "\n")
    print("Correy: " + (fcorrey) + " " +  str(correy_votes) + '\n')
    print("Li: " + (fli) + " " +  str(li_votes) + "\n")
    print("O'Tooley: " + (fotooley) + " " +  str(otooley_votes) + "\n")
    print("----------------------" + "\n")
    print("Winner: " + str(winner) + "\n")
    print("----------------------" + "\n")
        
    




