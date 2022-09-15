
import dpkt
import socket
from dpkt.tcp import TCP
from dpkt.udp import UDP
from dpkt.igmp import IGMP
from prettytable import PrettyTable


def mean_p_len(data_list) -> float:
    """ A function to determine the mean length of packet"""
    total_len = 0
    for item in data_list:
        total_len += item[1]
    mean_len = total_len / len(data_list)
    return round(mean_len, 2)


def main(pcap_file):
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
        #protocol = ip.p
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
    # Create a summary table of the parsed pcap files
    # https://www.geeksforgeeks.org/how-to-make-a-table-in-python/
    summary = PrettyTable(
        ["Student Name", "Number of Packets", "First Timestamp", "Last Timestamp", "Mean Packet Length"])
    if len(tcp_list) > 0:
        summary.add_row(["TCP", len(tcp_list), tcp_list[0][0], tcp_list[-1][0], mean_p_len(tcp_list)])
    if len(udp_list) > 0:
        summary.add_row(["UDP", len(udp_list), udp_list[0][0], udp_list[-1][0], mean_p_len(udp_list)])
    if len(igmp_list) > 0:
        summary.add_row(["IGMP", len(igmp_list), igmp_list[0][0], igmp_list[-1][0], mean_p_len(igmp_list)])
    if len(other_list) > 0:
        summary.add_row(["OTHER", len(other_list), other_list[0][0], other_list[-1][0], mean_p_len(other_list)])
    print(summary)
    # Return the necessary data for processing.
    return uri_data, tcp_data, ip_add, timestamp


if __name__ == "__main__":
    main()

    
        



