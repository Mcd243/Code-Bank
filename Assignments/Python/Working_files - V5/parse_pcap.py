import socket
import dpkt


def parser(pcap_file):
    """Parser function. Extracts the relevant data from the packets. TCP data has an extended data capture for later
    processing. Packet types are dynamically assigned to a dictionary with the relevant data to form a summary table
    for the packet capture file."""
    # initialize an empty list for the packet data to be stored
    packets = []
    tcp_data = []
    uri_data = []
    ip_add = []
    # Collect timestamps
    timestamp = []
    # Create a list of protocol numbers.
    protocol_number = []
    for num in range(0, 143):
        protocol_number.append(num)
    # Create a list of protocols
    protocol_list = ["HOPOPT", "ICMP", "IGMP", "GGP", "IPv4", "ST", "TCP", "CBT", "EGP", "IGP", "BBN-RCC-MON", "NVP-II",
                     "PUP", "ARGUS", "EMCON", "XNET", "CHAOS", "UDP", "MUX", "DCN-MEANS", "HMP", "PRM", "XNS-IDP",
                     "TRUNK-1", "TRUNK-2", "LEAF-1", "LEAF-2", "RDP", "IRTP", "ISO-TP4", "NETBLT", "MFE-NSP",
                     "MERIT-INP", "DCCP", "3PC", "IDPR", "XTP", "DDP", "IDPR-CMTP", "TP++", "IL", "IPv6", "SDRP",
                     "IPv6Route", "IPv6-Frag", "IDRP", "RSVP", "GRE", "DSR", "BNA", "ESP", "AH", "I-NLSP", "SWIPE",
                     "NARP", "MOBILE", "TLSP", "SKIP", "IPv6-ICMP", "IPv6-NoNxt", "IPv6Opts", "", "CFTP", "",
                     "SAT-EXPAK", "KRYPTOLAN", "RVD", "IPPC", "", "SAT-MON", "VISA", "IPCV", "CPNX", "CPHB", "WSN",
                     "PVP", "BR-SAT-MON", "SUN-ND", "WB_MON", "WB-EXPAK", "ISO_IP", "VMTP", "SECURE-VMTP", "VINES",
                     "TTP", "IPTM", "NSFNET-IGP", "DGP", "TCF", "EIGRP", "OSPFIGP", "Sprite_RPC", "LARP", "MTP",
                     "AX.25", "IPIP", "MICP", "SCC_SP", "ETHERIP", "ENCAP", "", "GMTP", "IFMP", "PNNI", "PIM", "ARIS",
                     "SCPS", "QNX", "A/N", "IPComp", "SNP", "Compaq-Peer", "IPX_in-IP", "VRRP", "PGM", "", "L2TP",
                     "DDX", "IATP", "STP", "SRP", "UTI", "SMP", "SM", "PTP", "ISIS over IPv4", "FIRE", "CRTP", "CRUDP",
                     "SSCOPMCE", "IPLT", "SPS", "PIPE", "SCTP", "FC", "RSVP_E2E_IGNORE", "Mobility Header", "UDPLite",
                     "MPLS-in-IP", "manet", "HIP", "Shim6", "WESP", "ROHC", "Ethernet"]
    # Create a protocol dictionary from a list of protocol types and a list of protocol numbers.
    proto_dict = dict(zip(protocol_number, protocol_list))
    # A dictionary to store protocol types and their data, found in the packet capture file.
    summary_data = {}
    # Initialise "TCP" in the summary_data dictionary.
    summary_data.setdefault("TCP", [])
    # Open the pcap file and read it.
    open_file = open(pcap_file, "rb")
    pcap = dpkt.pcap.Reader(open_file)
    # https: // jon.oberheide.org / blog / 2008 / 10 / 15 / dpkt - tutorial - 2 - parsing - a - pcap - file /
    # Jon Oberheide
    # Wednesday, October 15, 2008
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
        if ip.p == 6:
            print("TCP")
            info = [ts, len(buf)]
            key = proto_dict[ip.p]
            summary_data[key].append(info)
            tcp_data.append(tcp)
            # If the packet is a web request, add the URI's to a list.
            if tcp.dport == 80 and len(tcp.data) > 0:
                http = dpkt.http.Request(tcp.data)
                uri_data.append(http.uri)
        # https://stackoverflow.com/questions/20585920/how-to-add-multiple-values-to-a-dictionary-key-in-python
        # President James K. Polk
        # Dec 14 '13 at 17:08
        # If the ip protocol type is not in proto_dict then create a new key value pair in the summary_data dictionary
        # and append the info to the value list
        elif ip.p in proto_dict.keys():
            if proto_dict[ip.p] not in summary_data:
                info = [ts, len(buf)]
                key = proto_dict[ip.p]
                summary_data.setdefault(key, [])
                summary_data[key].append(info)
            # Append the info to the value list in summary_data for the protocol type key.
            else:
                info = [ts, len(buf)]
                key = proto_dict[ip.p]
                summary_data[key].append(info)
        # Catch an exception.
        else:
            print("Protocol not recognized")
    open_file.close()
    return uri_data, tcp_data, ip_add, timestamp, summary_data


def pcap_parser(pcap_file):
    """ Pass the pcap file to the parser function and collect the relevant data. Compile the data into various
     data objects to be used in further functions. The results are returned in a dictionary for later processing."""
    # Pass the pcap file to the parser
    uri_data, tcp_data, location_data, stats_data, summary_data = parser(pcap_file)
    # Group the relevant data for their respective functions.

    search_data = [tcp_data, uri_data]
    # Create a dictionary to reference modules to their relevant data.
    data_dict = {"summary_mod": summary_data,
                 "search_mod": search_data,
                 "stats_mod": stats_data,
                 "location_mod": location_data}
    return data_dict


if __name__ == "__main__":
    parser()
