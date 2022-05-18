#!/usr/bin/python3
## Ensure the clock is set correctly on the machine
## run as root and chmod the python script

import os, signal
import time

def stopped():
    name = "nmap"
    try:
        for line in os.popen("ps ax | grep " + name + " | grep -v grep"):
            fields = line.split()
            pid = fields[0]
            os.kill(int(pid), signal.SIGKILL)
            print("##############################\nStopped scanning successfully because not in scanning time window\n##############################")
    except:
        print("Error while running script")
## TEST
minute = int(input("What minute should it stop?: "))
## REMmove above

userInput = input("##############################\nDo you want to start a new scan or resume an existing one? (Please type new or resume only):\n")
if userInput == "resume" or userInput == "Resume" or userInput == "RESUME":
    resumeName = input("##############################\nPlease enter the exact .gnmap file you wish to resume scanning (include the .gnmap):\n")
    print("##############################\nResuming scan for " + resumeName)
    os.system("sudo nmap --resume " + resumeName + " &")
if userInput == "new" or userInput == "New" or userInput == "NEW":
    ipRange = input("##############################\nWhat IP Subnet range do you want to scan? (Example Usage: Enter like this: 10.10.0.0/16, 10.0.0.0, etc.):\n")
    outputName = input("##############################\nWhat naming convention do you want?:\n")
    protocol = input("##############################\nWhat protocol do you want to scan? (i.e., choose TCP, UDP, or SCTP only in lowercase):\n")
    if protocol == "tcp":
## Change below parameters for nmap that you want to run
        os.system("sudo nmap -v -n -sS -T4 -p- -sV -oA " + outputName + " " + ipRange + " &")
    if protocol == "udp":
        os.system("sudo nmap -v -n -sU -T4 --top-ports 10 -sV -oA " + outputName + " " + ipRange + " &")
    if protocol == "sctp":
        os.system("sudo nmap -v -n sY -T4 --top-ports 100 -sV -oA " + outputName + " " + ipRange + " &")


## Infinite loop to keep checking hour of the day until it reaches midnight 
while True:
    localT = time.localtime() 
    timeConvert = int(time.strftime("%M", localT)) 
    if timeConvert == minute:
        stopped()