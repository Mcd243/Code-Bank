"""
Created on Wed Oct 27 15:31:35 2021

@author: RickyP
"""

import os
import re
from parse_pcap import pcap_parser
from pcap_summary import summary_table
from pcap_search import search
from pcap_stats import stats
from pcap_location import locateip


print("Listing all .pcap files in the current directory \n")
files = os.listdir()

# Choose which pcap file to open
n = 0
file_dict = {}
flag = True
print("[Number]   Filename")
for file in files:
    if re.search(r"\.pcap$", file):
        n += 1
        file_dict[n] = file
        print(f"   [{n}]     {file}")


# Get the users choice of pcap file
while flag:
    choice = input("Enter the number of the filename you want to parse or enter x to quit: ")
    if choice == "x":
        flag = False
    elif re.search(r"[0-9]+", choice):
        if int(choice) in file_dict:
            print(f"\nParsing: {file_dict[int(choice)]} ...")
            pcap_file = file_dict[int(choice)]
            flag = False
            # Pass the pcap file to the function and store the relevant data in a dictionary that references the
            # data from the parser to their relevant modules.
            parsed_data_dict = pcap_parser(pcap_file)
            # print(packet_data)
    else:
        print("The number you have entered is not in the list.")
# Print out the summary table.
input(f"Press enter to print out the summary table for {pcap_file}...")
summary = summary_table(parsed_data_dict["summary_mod"])
print(summary)

# Extracts unique email addresses in the From: and To: fields of tcp data and prints them out.
# Extracts image uri's from http headers in packets and returns a table.
input(f"""Press enter to see unique email addresses in the From: and To: fields and image uri's from http headers
from {pcap_file}...""")
search(parsed_data_dict["search_mod"])

# Choose which pcap file to open
n = 0
db_dict = {}
flag = True
print("\nListing all location database files in the current working directory:")
print("[Number]   Filename")
for file in files:
    if re.search(r"\.mmdb$", file):
        n += 1
        db_dict[n] = file
        print(f"   [{n}]     {file}")
while flag:
    choice = input("\nEnter the number of the database you want to query or enter x to quit: ")
    if choice == "x":
        flag = False
    elif re.search(r"[0-9]+", choice):
        if int(choice) in db_dict:
            print(f"\nYou chose to create a KML file from: {db_dict[int(choice)]} ...")
            db_file = db_dict[int(choice)]
            flag = False
            # Pass the pcap file to the function and store the relevant data in a dictionary that references the
            # data from the parser to their relevant modules.
            locateip(db_file, parsed_data_dict["location_mod"])
            # print(packet_data)
    else:
        print("You have not entered a valid input.")
        print("Enter the number of the database you want to query or enter x to quit:")
