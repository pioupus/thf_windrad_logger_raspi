#!/usr/bin/env python 
import subprocess
import os


SERVICE_TARGET = "/etc/systemd/system/"
LOCAL_SERVICE_DIRECTORY = "../etc/systemd/system/"
def get_services_in_local_folder(list_of_current_services):
    service_directory = LOCAL_SERVICE_DIRECTORY
    for filename in os.listdir(service_directory):
        if filename.endswith(".system"):
            if not filename in list_of_current_services: #avoid duplicates
                list_of_current_services.append(filename)
            
    return list_of_current_services






subprocess.Popen("git fetch", shell=True,stdout=subprocess.PIPE).stdout.read()
git_commits_newer_than_local = subprocess.Popen("git log HEAD..origin/master", shell=True,stdout=subprocess.PIPE).stdout.read()
print(git_commits_newer_than_local)

if git_commits_newer_than_local == "":
    print("no new commit")
else:
    
    print("there are new commits")
    list_of_extra_services_fn = "list_of_services.txt"
    list_of_extra_services = []
    if os.path.isfile(list_of_extra_services_fn):
        with open(list_of_extra_services_fn, 'r') as list_of_extra_services_file:
            list_of_extra_services = [line.strip() for line in list_of_extra_services_file.readlines()]

    print("list of extra services: "+list_of_extra_services)
    list_of_current_services = get_services_in_local_folder([])            
    print("list of current services: "+list_of_current_services)
    
    list_services = list_of_extra_services.append(list_of_current_services)
    for service_name in list_of_services:
        service_name = service_name.split('#', 1)[0].strip() #delete comments of list of service file
        if service_name == "":
            continue
        print("stopping service: "+service_name)
        subprocess.call('echo $MY_PASSWORD | sudo systemctl stop '+ service_name, shell=True, stdout=subprocess.PIPE).stdout.read()
        
    
    git_pull_output = subprocess.Popen("git pull", shell=True,stdout=subprocess.PIPE).stdout.read()
    print("git pull:\n"+git_pull_output)
    run_once_file_output = subprocess.Popen('run_run_once_files.py', shell=True,stdout=subprocess.PIPE).stdout.read()
    print("git pull:\n"+run_once_file_output)
    
    list_of_current_services = get_services_in_local_folder([list_of_current_services])
    list_services = list_of_extra_services.append(list_of_current_services)
    for service_name in list_of_services:
        service_name = service_name.split('#', 1)[0].strip() #delete comments of list of service file
        if service_name == "":
            continue
        print("copy file: "+LOCAL_SERVICE_DIRECTORY+service_name+' to '+ SERVICE_TARGET+service_name)
        subprocess.call('echo $MY_PASSWORD | sudo sudo cp 'LOCAL_SERVICE_DIRECTORY+service_name+' '+ SERVICE_TARGET+service_name, shell=True, stdout=subprocess.PIPE).stdout.read()
        print("starting service: "+service_name)
        subprocess.call('echo $MY_PASSWORD | sudo systemctl start '+ service_name, shell=True, stdout=subprocess.PIPE).stdout.read()
        print("enabling service: "+service_name)
        subprocess.call('echo $MY_PASSWORD | sudo systemctl enable '+ service_name, shell=True, stdout=subprocess.PIPE).stdout.read()
