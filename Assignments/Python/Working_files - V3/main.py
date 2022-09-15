"""
Created on Wed Oct 27 15:31:35 2021

@author: RickyP
"""

import os
import re
from parsepcap import parser
from ProcessData import main


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
            print(f"\nPasrsing {file_dict[int(choice)]} ...\n")
            pcap_file = file_dict[int(choice)]
            flag = False
            # Pass the pcap file to the function and store the relevant data.
            uri_data, tcp_data, ip_add, timestamp, tcp_list, udp_list, igmp_list, other_list = parser(pcap_file)
            # print(packet_data)
    else:
        print("The number you have entered is not in the list.")
main(uri_data, tcp_data, ip_add, timestamp, tcp_list, udp_list, igmp_list, other_list)

