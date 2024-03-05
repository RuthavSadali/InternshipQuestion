import json # imports json module


importfile = open('C:\\Users\\rutha\\OneDrive\\Documents\\InterviewQuestion\\file.json', "r") # assumes that the file is in the same location as this program


data = json.load(importfile) # stores the json into data variable

names = [] # list for names. using list and not dictionary since dictionary does not allow duplicates
score = [] # list for applicant scores.

# assuming that 10 is the maximum value for each attribute
# intelligence will have weight of 30%
# strength will have weight of 10%
# endurance will have weight of 20%
# spicy food intelligence will have weight of 40% since it is the most important

for i in data['applicants']: #iterates through each applicant and calculates each score and stores the names and scores
    names.append(i['name'])
    score.append((0.03*i['attributes']['intelligence'])+(0.01*i['attributes']['strength'])+(0.02*i['attributes']['endurance'])+(0.04*i['attributes']['spicyFoodTolerance']))

dictpairs = zip(names, score) # combines the names and scores into key value pairs
output = dict(dictpairs) # turns the key value pairs into a dictionary
newdict = {'scoredApplicants':output}

jsonoutput = json.dumps(newdict, indent = 4) # 'dumps' the dictionary into a json template

with open("C:\\Users\\rutha\\OneDrive\\Documents\\InterviewQuestion\\scoredApplicants.json", "w") as outfile:
    outfile.write(jsonoutput) # outputs the final results into a json file at the given location

outfile.close() #closes both files since everything is done
importfile.close()