import os
import csv

#PyPollcsv = os.path.join ("Resources", "election_data.csv")
PyPollcsv = "c:/Users/PeiPei68/Desktop/HW2/Python-challenge/election_data.csv"

number_votes = 0
candidates = []
vote_counts = 0
percentages = []
Total_votes = 0
candidate_votes = {}
winning_candidate =''
winning_count = 0
with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    csv_header = next(csvreader)

    print(csvreader)

    for row in csvreader :
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name) 
            candidate_votes[candidate_name]=0
        
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        Total_votes = Total_votes + 1
        


output_file = "c:/Users/PeiPei68/Desktop/HW2/Python-challenge/election_data_revised.txt"

with open (output_file, "w") as txtfile:
    txtfile.write("Election Results")
    txtfile.write("...............................\n")
    txtfile.write("Total Votes:"+ str(Total_votes)+"\n")
    txtfile.write("................................\n")
    

    for candidate in candidate_votes:

        votes= candidate_votes.get(candidate)
        vote_percentage = float ( votes)/float (Total_votes) * 100
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate

    voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
    print(voter_output)
    print(".............................")

    
    txtfile.write(voter_output)
    txtfile.write("..............................\n")
    txtfile.write("winner:"+ winning_candidate + "\n") 
    txtfile.write("...............................\n")
    


    


