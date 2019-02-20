import requests
import json


#retrieve 

#You should write a function that will take as input a GitHub user ID. 
def GitZeHub (ID):
    #set up ID
    url = "https://api.github.com/users/" + ID + "/repos"
    repos = requests.get(url)
    reposNames = repos.json()
    # list of the names of the repositories that the user has
    # number of commits that are in each of the listed repositories.
    myList = []
    for item in reposNames:
        commitURL = "https://api.github.com/repos/"+ ID + "/" + item["name"] + "/commits"
        commit = requests.get(commitURL)
        commitString = json.loads(commit.text)
        comLength = len(commitString)

        #display ID, Repo, and Number of Commits
        print("User ID: " + ID + "Repository: " + item["name"] + "Number of commits: " + str(comLength))

        myList.append(str(item["name"]), comLength)
    
    return myList

if __name__ == "__main__":
    GitZeHub("nnekaou")
    GitZeHub("richkempinski")
