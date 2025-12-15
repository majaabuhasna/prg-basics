import json

filename = 'voting.json'
votes = {}

try:
    with open(filename, 'r') as file:
        votes = json.load(file)
except FileNotFoundError:
    print("File not found. Creating a new voting record.")
    votes = {}

person_name = input('Name of the person you are voting for: ').strip()

if person_name:
    votes[person_name] = votes.get(person_name, 0) + 1
    print(f"Vote recorded for {person_name}. Total votes: {votes[person_name]}")
else:
    print("Invalid name entered.")

with open(filename, 'w') as file:
    json.dump(votes, file, indent=4) 

print("Voting data saved successfully.")