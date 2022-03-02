#!/usr/bin/env python3
"""Alta3 Research | RZFeeser@alta3.com
   Moving files with SFTP"""

## import paramiko so we can talk SSH
import paramiko
import os

while True:
    where= input("Which machine would you like to connect to?\n")
    try:
        t = paramiko.Transport(where, 22) ## IP and port
    except:
        print("Connection could not be established.")
        continue
    break
## where to connect to
#t = paramiko.Transport("10.10.2.3", 22) ## IP and port
while True:
    who= input('Please enter the username.\n')
    know= input('Please enter the password.\n')
#try:
    try:
        t.connect(username=who, password=know)
        break
    except:
        print("Username or password incorrect.")
        continue
#except:
 #   print("Connection could not be established".)
## how to connect (see other labs on using id_rsa private/public keypairs)
#t.connect(username="bender", password="alta3")

## Make an sftp connection object
sftp = paramiko.SFTPClient.from_transport(t)

folder= input("What folder would you like to move the files into?")

## iterate across the files within directory
for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
  if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
    sftp.put(f"/home/student/filestocopy/"+x, "/{folder}/"+x) # move file to target location

## close the connections
sftp.close() # close the connection
t.close()
