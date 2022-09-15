"""
Created on Wed Oct 27 15:31:35 2021

@author: RickyP
"""
from prettytable import PrettyTable
from collections import Counter
import geoip2.database
import simplekml


def ip_data(ip_add):
    """This function takes in a list of tuples of ip addresses """
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
    return dst_dict, src_dict


def create_kml(data_b, dst_dict: dict):
    try:
        #data_b = "GeoLite2-City_20190129.mmdb"
        reader = geoip2.database.Reader(fr"{data_b}")
    except FileNotFoundError as error:
        print(error)
        print(f'The {data_b} file cannot be found')
    location_data = []
    # Define KML object
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
    return kml


def locateip(db_file, ip_add):
    dst_dict, src_dict = ip_data(ip_add)
    src_table = PrettyTable(
        ["   Source IP   ", "  Number of packets sent  "])
    for key in sorted(src_dict, reverse=True):
        src_table.add_row([src_dict[key], key])
    input("\nPress enter to view the source IP table.")
    print(src_table)
    dst_table = PrettyTable(
        ["Destination IP", "Number of packets received"])
    for key in sorted(dst_dict, reverse=True):
        dst_table.add_row([dst_dict[key], key])
    input("\nPress enter to view the destination IP table.")
    print(dst_table)
    pcap_kml = create_kml(db_file, dst_dict)
    input("\nPress enter to view the destination IP KML object.")
    print(pcap_kml.kml())


if __name__ == "__main__":
    locateip()
