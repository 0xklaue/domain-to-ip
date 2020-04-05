# domain-to-ip
Python script to get IPs from domain names

# Usage

`kali@kali:~$ python domains-to-ip.py | tee -a ip-addresses`

Note: Make sure to change the filename in the script from `domains` if you have a different file name.

# About
This script is used when you have 100s of domains / subdomains and would like to get their IPv4 addresses for passing it to nmap / masscan for further enumeration.

# Requirements
Python v2
