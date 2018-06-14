#!/usr/bin/env python 
import subprocess

subprocess.Popen("git fetch", shell=True,stdout=subprocess.PIPE).stdout.read()
git_commits_newer_than_local = subprocess.Popen("git log HEAD..origin/master", shell=True,stdout=subprocess.PIPE).stdout.read()
print(git_commits_newer_than_local)

if git_commits_newer_than_local == "":
    print("no new commit")
else:
    print("there are new commits")
    subprocess.Popen("git pull", shell=True,stdout=subprocess.PIPE).stdout.read()
