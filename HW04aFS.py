""" The purpose of this assignment is to write a function that will take an input of a GitHub user ID 
and have the output of the names of repositories that the user has along with the number of commits in the repositories. """

import requests
import json

def rep_comm(gh):
    total = dict()
    url = "https://api.github.com/users/"+gh+"/repos"
    reposit = requests.get(url)
    repos = reposit.json()
    for repo in repos:
        urls = "https://api.github.com/repos/"+gh+"/"+repo['name']+"/commits"
        obtain = requests.get(urls)
        commit = obtain.json()
        total[repo['name']] = len(commit)
    return total

def main():
    gh = input("Enter a valid GitHub username. ")
    total = rep_comm(gh)
    for r,c in total.items():
        print("Repo:",r,"Number of commits:",c)

if __name__ == '__main__':
    main()
