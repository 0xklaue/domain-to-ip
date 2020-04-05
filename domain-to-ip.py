#!/usr/bin/python

import sys
import socket

read_file = open('domains','r')

for host in read_file:
    try:
        print socket.gethostbyname(host.rstrip("\n"))   #rstrip for removing new line characters
    except socket.gaierror:
        print("Domain " + host + " not found. Please verify manually.")

read_file.close()
