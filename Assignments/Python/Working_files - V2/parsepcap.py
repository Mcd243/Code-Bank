import dpkt
import socket
from dpkt.tcp import TCP
from dpkt.udp import UDP
from dpkt.igmp import IGMP
from prettytable import PrettyTable
from datetime import datetime


def parser(pcap_file):
    """main function. Extracts the relevant data from the packets"""
    # open the pcap file and read it
    open_file = open(pcap_file, "rb")
    pcap = dpkt.pcap.Reader(open_file)
    # initialize an empty list for the packets to be stored
    packets = []
    tcp_data = []
    uri_data = []
    ip_add = []
    # initialize list as to differentiate packet types
    tcp_list = []
    udp_list = []
    igmp_list = []
    other_list = []
    #collect timestamps
    timestamp = []
    # Iterate through the packets and add the contents to the appropriate lists.
    for ts, buf in pcap:
        # Create a timestamp and packet data tuple for each packet
        timestamp.append(ts)
        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data
        tcp = ip.data
        packets.append(eth)
        # Collect the ip addresses and add them to a list
        ip_add.append((socket.inet_ntoa(ip.src), socket.inet_ntoa(ip.dst)))
        if type(ip.data) == TCP:
            info = [ts, len(buf)]
            tcp_list.append(info)
            tcp_data.append(tcp)
            # If the packet is a web request, add the URI's to a list.
            if tcp.dport == 80 and len(tcp.data) > 0:
                http = dpkt.http.Request(tcp.data)
                uri_data.append(http.uri)
        # Add UDP data to a list.
        elif type(ip.data) == UDP:
            info = [ts, len(buf)]
            udp_list.append(info)
        # Add the IGMP data to a list
        elif type(ip.data) == IGMP:
            info = [ts, len(buf)]
            igmp_list.append(info)
        else:
            info = [ts, len(buf)]
            other_list.append(info)
    open_file.close()
    return uri_data, tcp_data, ip_add, timestamp, tcp_list, udp_list, igmp_list, other_list

    # Create a summary table of the parsed pcap files
    # https://www.geeksforgeeks.org/how-to-make-a-table-in-python/
#    summary = PrettyTable(
#        ["Student Name", "Number of Packets", "First Timestamp", "Last Timestamp", "Mean Packet Length"])
#    if len(tcp_list) > 0:
#        summary.add_row(["TCP", len(tcp_list), ts_convert(tcp_list[0][0]), ts_convert(tcp_list[-1][0]), mean_p_len(tcp_list)])
#    if len(udp_list) > 0:
#        summary.add_row(["UDP", len(udp_list), ts_convert(udp_list[0][0]), ts_convert(udp_list[-1][0]), mean_p_len(udp_list)])
#    if len(igmp_list) > 0:
#        summary.add_row(["IGMP", len(igmp_list), ts_convert(igmp_list[0][0]), ts_convert(igmp_list[-1][0]), mean_p_len(igmp_list)])
#    if len(other_list) > 0:
#        summary.add_row(["OTHER", len(other_list), ts_convert(other_list[0][0]), ts_convert(other_list[-1][0]), mean_p_len(other_list)])
#    print(summary)


    # Return the necessary data for processing.
    #return uri_data, tcp_data, ip_add, timestamp


if __name__ == "__main__":
    main()
