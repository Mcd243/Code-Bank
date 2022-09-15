"""
Created on Wed Oct 27 15:31:35 2021

@author: RickyP
"""

import os
import re
# IP addresses
from prettytable import PrettyTable

from my_parse_pcap1 import main
# Ip address section
from collections import Counter
# Geolocation
import geoip2.database
# Geolocation
import simplekml
# stats

import matpotlib.pyplot

def find_email(data):
    """Extract email addresses from """
    try:
        match = re.findall(r"From: \"[a-zA-Z]+ [a-zA-Z]+\" <\w+@\w+\.\w+>|FROM: <\w+@\w+\.\w+>|TO: <\w+@\w+\.\w+>|To: <\w+@\w+\.\w+>", data)
        return match
    except Exception as err:
        print(err)

def find_image(data):
    """Extract email addresses from """
    try:
        match = re.findall(r"[-\/\w]+.gif|[-\/\w]+.jpg|[-\/\w]+.png", data)
        return match
    except Exception as err:
        print(err)


#######################################################################################################################

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
            uri_data, tcp_data, ip_add, timestamp = main(pcap_file)
            #print(packet_data)
    else:
        print("The number you have entered is not in the list.")

#######################################################################################################################

# Pass the tcp_data to the find_email function to search for emails.
emails = find_email(str(tcp_data))

# Clean up the output of the find_email() function and display distinct email addresses.
from_list = []
to_list = []
for item in emails:
    if emails.index(item) % 2 == 0:
        from_list.append(item)
    else:
        to_list.append(item)
if len(from_list) > 0:
    from_set = set(re.findall(r"\w+@\w+\.\w+", str(from_list)))
    print("\nEmail addresses present in the From: field are listed below: ")
    for email in from_set:
        print(f"[*]    From: {email}")
else:
    print("There are no email addresses present in the From: field")

if len(to_list) > 0:
    to_set = set(re.findall(r"\w+@\w+\.\w+", str(to_list)))
    print("\nEmail addresses present in the To: field are listed below: ")
    for email in to_set:
        print(f"[*]      To: {email}")
else:
    print("There are no email addresses present in the To: field")

#######################################################################################################################
# Find images in the uri_data
images = find_image(str(uri_data))
# Display a list of file paths and file names.
if len(images) > 0:
    print("\n Below are listed all the file paths and file names.\n")
    image_table = PrettyTable(
        ["Full File Path", "File Name"])
    for file in images:
        image_table.add_row([file, (os.path.basename(file))])
else:
    print("No images were found.")

image_table = PrettyTable(
        ["Full File Path", "File Name"])
for file in images:
    image_table.add_row([file, (os.path.basename(file))])

print(image_table)

#######################################################################################################################

cnt = Counter()

src_dict = {}
for srcip, dstip in ip_add:
    cnt[srcip] += 1
for ip, count in cnt.items():
    src_dict[count] = ip


dst_dict = {}
for srcip, dstip in ip_add:
    cnt[dstip] += 1
for ip, count in cnt.items():
    dst_dict[count] = ip

src_table = PrettyTable(
        ["   Source IP   ", "  Number of packets sent  "])
for key in sorted(src_dict, reverse=True):
    src_table.add_row([src_dict[key], key])
print(src_table)
dst_table = PrettyTable(
     ["Destination IP", "Number of packets received"])
for key in sorted(dst_dict, reverse=True):
    dst_table.add_row([dst_dict[key], key])
print(dst_table)

######################################################################################################################

try:
    data_b = "GeoLite2-City_20190129.mmdb"
    reader = geoip2.database.Reader(fr"{data_b}")
except FileNotFoundError as error:
    print(error)
    print(f'The {data_b} file cannot be found')

location_data = []
#define KML object
kml = simplekml.Kml()
for key in dst_dict:
    try:
        rec = reader.city(dst_dict[key])
        kml.newpoint(name=dst_dict[key], coords=[(rec.location.longitude, rec.location.latitude)],
            description=f"""Country: {rec.country.name} \n 
            City: {rec.city.name} \n
            Packets sent to this location: {key}""")
    except Exception as error:
        print(error)
# save as a file and print contents to stdout
kml.save("packet_destinations.kml")
print(kml.kml())

######################################################################################################################


first = (round(timestamp[0], -1))
last = (round(timestamp[0], -1) + 10)

timestamp_list = []
inner_list = []
no_packets_list = []
time_grouping = 5

for time in timestamp:
    if first <= time < last:
        inner_list.append(time)
    elif time >= last:
        first = last
        last += time_grouping
        timestamp_list.append(inner_list[1])
        no_packets_list.append(len(inner_list))
print(timestamp_list)
print(no_packets_list)
time_packets = tuple(zip(timestamp_list, no_packets_list))
print(time_packets)

#protocol = ip.p

