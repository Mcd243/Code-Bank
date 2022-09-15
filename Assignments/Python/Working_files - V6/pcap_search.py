"""
Created on Wed Oct 27 15:31:35 2021

@author: Muun Macdonald
"""
import sys
import os
import re
from prettytable import PrettyTable


def find_email(data):
    """Extract email addresses from tcp packet data. """
    try:
        match = re.findall(
            r"/from:\s?\"[a-zA-Z]+ [a-zA-Z]+\" <\w+@\w+\.\w+>|from:\s?<\w+@\w+\.\w+>|TO:\s?<\w+@\w+\.\w+>|to:\s?\w+@\w+"
            r"\.\w+/gmi",
            data)
        return match
    except Exception as err:
        print(err)


def find_emails(tcp_data: list):
    """Finds email addresses in tcp data and returns a set of unique email-addresses form the From: field and
     returns a set of unique email-addresses form the To: field"""
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
        # Strips the email address from redundant data.
        from_set = set(re.findall(r"\w+@\w+\.\w+", str(from_list)))
        from_list = list(from_set)
    else:
        print("There are no email addresses present in the From: field")
    if len(to_list) > 0:
        # Strips the email address from redundant data.
        to_set = set(re.findall(r"\w+@\w+\.\w+", str(to_list)))
        to_list = list(to_set)
    else:
        print("There are no email addresses present in the To: field")
    return from_list, to_list


def find_image(data):
    """Extract image uri's in the http headers of packets."""
    try:
        match = re.findall(r"[-/\w]+.gif|[-/\w]+.jpg|[-/\w]+.png", data)
        return match
    except Exception as err:
        print(err)


def image_table(uri_data):
    """Creates a table of image uri's and their actual file names."""
    # Find images in the uri_data
    images = find_image(str(uri_data))
    # Display a list of file paths and file names.
    if len(images) > 0:
        print("\n Below are listed all the file paths and file names.")
        table = PrettyTable(
            ["Full File Path", "File Name"])
        for file in images:
            table.add_row([file, (os.path.basename(file))])
        return table
    else:
        print("No images were found.")


def search(packet_data):
    """Extracts unique email addresses in the From: and To: fields of tcp data and prints them out.
      Extracts image uri's from http headers in packets and returns a table"""
    try:
        from_emails, to_emails = find_emails(packet_data[0])
        input("\nPress enter to display all the unique email addresses in the pcap file in the From: field.")
        for email in from_emails:
            print(f"[*]    From: {email}")
        input("\nPress enter to display all the unique email addresses in the pcap file in the To: field.")
        for email in to_emails:
            print(f"[*]      To: {email}")
        input("\nPress enter to display all the http requests for image data.")
        img_table = image_table(packet_data[1])
        print(img_table)
    except ImportError as err:
        print(f"!! Import problem({err.__class__.__name__}) : {err}", file=sys.stderr)


if __name__ == "__main__":
    search()
