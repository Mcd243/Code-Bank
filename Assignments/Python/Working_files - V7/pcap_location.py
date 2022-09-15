"""
Created on Wed Oct 27 15:31:35 2021

@author: Muun Macdonald
"""
import sys
from prettytable import PrettyTable
import geoip2.database
import simplekml


def ip_data(ip_add):
    """This function takes in a list of tuples of ip addresses and returns a dictionary of unique ip address pairs
     as the key and the number of occurrences as the value."""
    unique_tup = []
    num_list = []
    # Collect all unique ip address pairs and store them in a list.
    for tup in ip_add:
        if tup not in unique_tup:
            unique_tup.append(tup)
    # Count the instances of each unique ip address pair in ip_add.
    for item in unique_tup:
        count = 0
        for tup in ip_add:
            if tup == item:
                count += 1
        # Add the count to a list of quantities
        num_list.append(count)
    # Create a dictionary from the two lists.
    ip_dict = dict(zip(unique_tup, num_list))
    # Sort the dictionary by value.
    # https://www.tutorialsteacher.com/articles/sort-dict-by-value-in-python
    # Malhar Lathkar
    # 06 Jan 2021
    iplist = sorted(ip_dict.items(), key=lambda x: x[1], reverse=True)
    sorted_dict = dict(iplist)
    return sorted_dict


def create_kml(data_b, dst_dict: dict):
    """Function that takes a database file and an IP destination dictionary and creates a KML file locating the
     destination IP addresses."""
    try:
        reader = geoip2.database.Reader(fr"{data_b}")
    except FileNotFoundError as error:
        print(error)
        print(f'The {data_b} file cannot be found')
    # Define KML object
    kml = simplekml.Kml()
    for key in dst_dict:
        try:
            rec = reader.city(key)
            kml.newpoint(name=key, coords=[(rec.location.longitude, rec.location.latitude)],
                         description=f"""Country: {rec.country.name} \n 
                City: {rec.city.name} \n
                Packets sent to this location: {dst_dict[key]}""")
        except Exception as error:
            print(error)
    # save as a file and print contents to stdout
    kml.save("packet_destinations.kml")
    return kml


def locateip(db_file, ip_add):
    """This is the main function. It sends ip addresses to the ip_data function for processing. A dictionary is
    returned and the results formatted in a table. Finally a kml file is created from the destination ip addresses."""
    try:
        # Process the ip data.
        ip_dict = ip_data(ip_add)
        # Lists to capture data for the kml creation
        dst_ip = []
        p_cnt = []
        # Create the table of processed ip data.
        ip_table = PrettyTable(
            ["   Source IP   ", " Destination IP ", "  Number of packets sent  "])
        for key in ip_dict:
            # Add rows to the table
            ip_table.add_row([key[0], key[1], ip_dict[key]])
            # Collect destination ip addresses and packet numbers in a dictionary.
            dst_ip.append(key[1])
            p_cnt.append(ip_dict[key])
        dst_dict = dict(zip(dst_ip, p_cnt))
        input("\nPress enter to view the IP table.")
        print(ip_table)
        # Create a Kml file ip data.
        pcap_kml = create_kml(db_file, dst_dict)
        input("\nPress enter to view the destination IP KML object.")
        print(pcap_kml.kml())
    except ImportError as err:
        print(f"!! Import problem({err.__class__.__name__}) : {err}", file=sys.stderr)
    except FileNotFoundError as err:
        print(f"!! Cannot open {db_file} ({err.__class__.__name__}) : {err}", file=sys.stderr)
    except OSError as err:
        print(f"!! System exception {db_file} ({err.__class__.__name__}) : {err}", file=sys.stderr)
    except TypeError as err:
        print(f"!! Input is the wrong type ({err.__class__.__name__}) : {err}", file=sys.stderr)
    except Exception as err:
        print(f"!! Exception ({err.__class__.__name__}) : {err}", file=sys.stderr)


if __name__ == "__main__":
    locateip()
