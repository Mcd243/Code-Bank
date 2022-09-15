"""
Created on Wed Oct 27 15:31:35 2021

@author: Muun Macdonald
"""

import os
import re
import sys
from parse_pcap import pcap_parser
from pcap_summary import summary_table
from pcap_search import search
from pcap_stats import stats
from pcap_location import locateip


print("Listing all .pcap files in the current directory \n")
files = os.listdir()
# Choose which pcap file to open
n = 0
# A dictionary to hold file_names
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
    try:
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
    except FileNotFoundError as err:
        print(f"!! There was a problem opening {pcap_file}({err.__class__.__name__}) : {err}", file=sys.stderr)
    except ImportError as err:
        print(f"!! Import problem({err.__class__.__name__}) : {err}", file=sys.stderr)
    except Exception as err:
        print(f"!! Exception ({err.__class__.__name__}) : {err}", file=sys.stderr)

# Print out the summary table.
input(f"Press enter to print out the summary table for {pcap_file}...")
try:
    summary = summary_table(parsed_data_dict["summary_mod"])
    print(summary)
except ImportError as err:
    print(f"!! Import problem({err.__class__.__name__}) : {err}", file=sys.stderr)
except Exception as err:
    print(f"!! Exception ({err.__class__.__name__}) : {err}", file=sys.stderr)

# Extracts unique email addresses in the From: and To: fields of tcp data and prints them out.
# Extracts image uri's from http headers in packets and returns a table.
input(f"""Press enter to see unique email addresses in the From: and To: fields and image uri's from http headers
from {pcap_file}...""")
try:
    search(parsed_data_dict["search_mod"])
except ImportError as err:
    print(f"!! Import problem({err.__class__.__name__}) : {err}", file=sys.stderr)
except Exception as err:
    print(f"!! Exception ({err.__class__.__name__}) : {err}", file=sys.stderr)

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
    try:
        choice = input("\nEnter the number of the database you want to query or enter x to quit: ")
        if choice == "x":
            flag = False
        elif re.search(r"[0-9]+", choice):
            if int(choice) in db_dict:
                print(f"\nYou chose to create a KML file from: {db_dict[int(choice)]} ...")
                db_file = db_dict[int(choice)]
                flag = False
                # Pass the database file to the locateip function.
                locateip(db_file, parsed_data_dict["location_mod"])
        else:
            print("You have not entered a valid input.")
            print("Enter the number of the database you want to query or enter x to quit:")
    except FileNotFoundError as err:
        print(f"!! There was a problem opening {pcap_file}({err.__class__.__name__}) : {err}", file=sys.stderr)
    except ImportError as err:
        print(f"!! Import problem({err.__class__.__name__}) : {err}", file=sys.stderr)
    except Exception as err:
        print(f"!! Exception ({err.__class__.__name__}) : {err}", file=sys.stderr)
try:
    # Run the stats module to output a graph
    stats(parsed_data_dict["stats_mod"])
except ImportError as err:
    print(f"!! Import problem({err.__class__.__name__}) : {err}", file=sys.stderr)
except Exception as err:
    print(f"!! Exception ({err.__class__.__name__}) : {err}", file=sys.stderr)
finally:
    print("There is problem running this program. Fail the student for gross mis-coding.")
