######### Reformat IP addresses into standard dotted decimal format ###########

ip_byte = b'\x92\xb0\xa4['
import socket
socket.inet_ntoa(ip_byte)

# '146.176.164.91'

#################################################################################

import socket, dpkt
from parse_pcap import main

packets = main(print_out=False, break_first=False)
#print(packets[0])

## Insert code here
for p in packets:
        ip = p.data
        tcp = ip.data
        print(f"{socket.inet_ntoa(ip.src)}:{tcp.sport} -> {socket.inet_ntoa(ip.dst)}:{tcp.dport}")
        #print("\n")

