#Automatisierung von Gitlab confs 
#1. Set Global Login Exports for GitlabLogin
#2. Clone confs so you need to just execute a pull in the script for reading in new inputs
# Should work right now needs some more Exception handling 

import os 
import time 
from git import Repo
import logging

PATH="" #Define Repo Path
repo = git.Repo(PATH)

def reload_nginx():
    print('reloading nginx')
    os.system('systemctl reload nginx')

def pulling_changes():
    repo.remotes.origin.pull()
    
def check_for_changes():
    #repo = git.Repo(path)
    current = repo.head.commit

    if current == repo.head.commit:
        print("Repo not changed. Going to sleep again zzzz")
        time.sleep(300) #Change this if you want faster actualisations

    else:
        print("Repo changed.Pulling changes")
        pulling_changes()
        print("Reload nginx")
        reload_nginx()
    
if __init__ == "__main__":
    while True:
        check_for_changes()
