"""
Created on Wed Oct 27 15:31:35 2021

@author: RickyP
"""

import os
import re
# IP addresses
from prettytable import PrettyTable

from parsepcap import parser

# Ip address section
from collections import Counter
# Geolocation
import geoip2.database
# Geolocation
import simplekml
# stats
from datetime import datetime

import matplotlib.pyplot as plt


def mean_p_len(data_list) -> float:
    """ A function to determine the mean length of packet"""
    total_len = 0
    for item in data_list:
        total_len += item[1]
    mean_len = total_len / len(data_list)
    return round(mean_len, 2)


def ts_convert(timestamp) -> datetime:
    """ A function to convert a timestamp to a datetime object."""
    # https://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date
    # Contango
    dt = datetime.fromtimestamp(timestamp)
    rezolved_dt = f"{dt:%Y-%m-%d %H:%M:%S}"
    return rezolved_dt


def summary_table(tcp_list, udp_list, igmp_list, other_list):
    # Create a summary table of the parsed pcap files
    # https://www.geeksforgeeks.org/how-to-make-a-table-in-python/
    summary = PrettyTable(
        ["Student Name", "Number of Packets", "First Timestamp", "Last Timestamp", "Mean Packet Length"])
    if len(tcp_list) > 0:
        summary.add_row(["TCP", len(tcp_list), ts_convert(tcp_list[0][0]), ts_convert(tcp_list[-1][0]), mean_p_len(tcp_list)])
    if len(udp_list) > 0:
        summary.add_row(["UDP", len(udp_list), ts_convert(udp_list[0][0]), ts_convert(udp_list[-1][0]), mean_p_len(udp_list)])
    if len(igmp_list) > 0:
        summary.add_row(["IGMP", len(igmp_list), ts_convert(igmp_list[0][0]), ts_convert(igmp_list[-1][0]), mean_p_len(igmp_list)])
    if len(other_list) > 0:
        summary.add_row(["OTHER", len(other_list), ts_convert(other_list[0][0]), ts_convert(other_list[-1][0]), mean_p_len(other_list)])
    return summary


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


def find_emails(tcp_data):
    """some stuff"""
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


def find_images(uri_data):
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


def ip_data(ip_add):
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
    return dst_dict


def create_kml(dst_dict):
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


def pcap_stats(timestamp):
    first = timestamp[0]
    last = timestamp[0]
    timestamp_list = []
    inner_list = []
    no_packets_list = []
    first_timestamp = []
    time_grouping = 10
    default = timestamp[0]
    first = timestamp[0]
    last = timestamp[0] + time_grouping

    for time in timestamp:
        if first <= time < last:
            inner_list.append(time)
        elif time > last:
            if len(inner_list) == 0:
                inner_list.append(default)
            else:
                first_timestamp.append(inner_list[0])
            timestamp_list.append(inner_list)
            no_packets_list.append(len(inner_list))
            inner_list = []
            first = last
            last += time_grouping


    print(no_packets_list)
    print(first_timestamp)

    print(len(no_packets_list))
    print(len(first_timestamp))

    #plt.plot(first_timestamp, no_packets_list, color='red', marker='o')
    #plt.title('Number of Packets Vs Time', fontsize=14)
    #plt.xlabel('Time', fontsize=14)
    #plt.ylabel('Number of Packets', fontsize=14)
    #plt.grid(True)
    #plt.show()


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
            #print(packet_data)
    else:
        print("The number you have entered is not in the list.")
# Print out the summary of the parsed pcap file.
summary = summary_table(tcp_list, udp_list, igmp_list, other_list)
print(summary)

# Find emails from the tcp data.
find_emails(tcp_data)

# Find images from uri data.
find_images(uri_data)

# Create a dictionary with distinct ip_address pairs
dst_dict = ip_data(ip_add)

# Create a kml file.
create_kml(dst_dict)

