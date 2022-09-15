import socket

import dpkt
from dpkt.igmp import IGMP
from dpkt.tcp import TCP
from dpkt.udp import UDP


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
    # Collect timestamps
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


if __name__ == "__main__":
    parser()
