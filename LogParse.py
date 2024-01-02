#!/usr/bin/python3
import re
import csv
import socket
from collections import Counter

NginxLog = "access.log"

# Define the regular expression for matching IP addresses
regexp = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"

# Read the Nginx log file
with open(NginxLog) as file:
    logs = file.read()

# Extract IP addresses using the regex pattern
IPList = re.findall(regexp, logs)

# Function for reverse DNS lookup
def reverse_dns_lookup(ip):
    try:
        host_name, _, _ = socket.gethostbyaddr(ip)
        return host_name
    except socket.herror:
        return "N/A"

# Create a CSV file for results
with open("finalresult.csv", "w", newline='') as file:
    WriteIntoTheCSV = csv.writer(file)
    WriteIntoTheCSV.writerow(["IPs List", "Number of Counts", "Reverse DNS"])

    # Iterate over the items in the Counter
    for IPs, Counts in Counter(IPList).items():
        # Perform reverse DNS lookup for each IP
        host_name = reverse_dns_lookup(IPs)
        WriteIntoTheCSV.writerow([IPs, Counts, host_name])
