import os
import csv

candidates = []
number_votes = 0
vote_counts = []
election_data = ['1', '2']
percentages = []
max_votes = vote_counts[0]
max_index = 0

for files in election_data:
    election_dataCSV = csvpath = os.path.join("election_data.csv")
      

with open(election_dataCSV) as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     line = next(csvreader,None)

    
     for line in csvreader:        
         number_votes = number_votes +1
         candidate = line[2]
          
         if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
   
         else:   
              candidates.append(candidate)
              vote_counts.append(1)
               
    
     for count in range(len(candidates)):
         vote_percentage = vote_counts[count]/number_votes*100
         percentages.append(vote_percentage)
        
         if vote_counts[count] > max_votes:
            max_votes = vote_counts[count]
            print(max_votes)
            max_index = count
    
     
         winner = candidates[max_index]

   
    
     print("Election Results")
     print("Total Votes:"+("number_votes"))
   
      


    output_file = os.path.join ("Resources","election_data_revised.csv")
    with open (output_file, "w") as txtfile:
        txtfile.write("Election Results\n")
        
      
      
    
  
    
   
