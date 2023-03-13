# Import the necessary libraries
import pandas as pd
import os

# Define the path to the election_data.csv file
file_path = os.path.join("Resources", "election_data.csv")

# Read in the CSV file as a pandas dataframe
df = pd.read_csv(file_path)

# Calculate the total number of votes cast
total_votes = len(df)

# Get a list of candidates who received votes and calculate the number of votes each candidate won
candidates = df["Candidate"].unique()
votes_per_candidate = df["Candidate"].value_counts()

# Calculate the percentage of votes each candidate won
vote_percentages = (votes_per_candidate / total_votes) * 100

# Get the name of the winner based on popular vote
winner = vote_percentages.idxmax()

results = f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""
for candidate in candidates:
    vote_percentage = vote_percentages[candidate]
    num_votes = votes_per_candidate[candidate]
    results += f"{candidate}: {vote_percentage:.3f}% ({num_votes})\n"
results += f"""-------------------------
Winner: {winner}
-------------------------
"""

# Print the results to the terminal
print(results)

# Write the results to a text file
with open("analysis/election_results.txt", "w") as text_file:
    text_file.write(results)