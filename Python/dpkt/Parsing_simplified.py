### https://jon.oberheide.org/blog/2008/10/15/dpkt-tutorial-2-parsing-a-pcap-file/ ###

# first open a pcap file and save as f
f = open('test.pcap')

# read the pcap file using the dpkt .Reader class. Use f as the argument and store as pcap
pcap = dpkt.pcap.Reader(f)


################ the unfriendly method ##############
# iterate over the pcap object to get a timestamp and packet data length
# ts is a timestamp 
# buf is the contants of the file
for ts, buf in pcap:
    print ts, len(buf)

1220901348.61 66
1220901348.68 66
.....

################ the friendly method #######################
############ using dpkt.ethernet.Ethernet(buf) #############
# parses the pcap data into an eth object which is easy to extract: 
# ip info
#     tcp info  - sender port
#               - destination port
#               - http data:
#                       - method
#                       - uri
#                       - verstion
#                       - headers


# get the timestamp and the packet data for each packet in pcap and store in eth
for ts, buf in pcap:
     eth = dpkt.ethernet.Ethernet(buf)

print eth

#Ethernet(src='\x00\x1a\xa0kUf', dst='\x00\x13I\xae\x84,', data=IP(src='\xc0\xa8\n\n',
#off=16384, dst='C\x17\x030', sum=25129, len=52, p=6, id=51105, data=TCP(seq=9632694,
#off_x2=128, ack=3382015884, win=54, sum=65372, flags=17, dport=80, sport=56145)))

### Extract the ip data from eth 
ip = eth.data
### Extract the tcp data from the ip data
tcp = ip.data
### Extract the port data from the tcp data
print tcp.sport
# 56145
print tcp.dport
# 80

######### Extract and decode HTTP requests (payload) ################
# for http requests the destination port must be 80
# the HTTP requests are in the tcp data

if tcp.dport == 80 and len(tcp.data) > 0:
     http = dpkt.http.Request(tcp.data)

print http.method
# GET

print http.uri
# /testurl

print http.version
# 1.1

print http.headers['user-agent']
# Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.5)

#######################################################################

#!/usr/bin/env python

import dpkt

f = open('test.pcap')
pcap = dpkt.pcap.Reader(f)

for ts, buf in pcap:
 eth = dpkt.ethernet.Ethernet(buf)
 ip = eth.data
 tcp = ip.data

 if tcp.dport == 80 and len(tcp.data) > 0:
 http = dpkt.http.Request(tcp.data)
 print http.uri

f.close()