################ INSTALL DPKT ##################################

import dpkt

!pip install dpkt

help(dpkt.ethernet.Ethernet)

############ Parsing pcap records using dpkt ###################

eth = dpkt.ethernet.Ethernet(buf)
ip = eth.data
tcp = ip.data 
sourcePort = tcp.sport

###working-eg###
# store the contenets of the packet(called by the min function)
eth=packets[0]

# extract the data to variable ip
ip = eth.data

# get the source ip(raw)
srcIP = ip.src
# get the destination(raw)
dstIP = ip.dst

# decode the IP address data
socket.inet_ntoa(srcIP)
socket.inet_ntoa(dstIP)

# ectract the data to variable tcp
tcp = ip.data

# get the source port and dest port from the data
print(f"{tcp.sport=}")
print(f"{tcp.dport=}")


########################################################################


from parse_pcap import main

packets = main(print_out=False, break_first=False)
eth=packets[0]

## Insert code here
## The code below helps us pull out the values automatically. It should only make sense once you have completed more the of the lab.
# Q17.1
print(f"{type(eth)=}")

# Q17.2
ip = eth.data
srcIP = ip.src
dstIP = ip.dst
#####what is this########
print(f"{srcIP=}") # this is binary, we can't read that easily

# convert:###i dont understand this fstatement
print(f"{socket.inet_ntoa(srcIP)=}")
print(f"{socket.inet_ntoa(dstIP)=}")


# Q17.3
tcp = ip.data
print(f"{tcp.sport=}")
print(f"{tcp.dport=}")

# Q17.4

# Not answered with code, check the packet encapsulation diagram in the slides


######################################################################
# parsing tutorial

# open pcap with Reader class
f = open('test.pcap')
pcap = dpkt.pcap.Reader(f)

# print timestamp and packet data length
for ts, buf in pcap:
    print(ts, len(buf))

#  pass a raw buffer to the appropriate dpkt class and have contents 
# automatically parsed and decoded into friendly python objects:


######################## TCP layer #########################
# parses and decodes into an eth object (TCP object)

for ts, buf in pcap:
     eth = dpkt.ethernet.Ethernet(buf)
# parses and decodes into an eth object
ip = eth.data
# parses and decodes into an TCP object
tcp = ip.data

# look at source port
print(tcp.sport)

# look at destination port
print(tcp.dport)

################# DECODE HTTP REQUESTS #####################

# if destination port is 80 and there is a destination port decode

if tcp.dport == 80 and len(tcp.data) > 0:
     http = dpkt.http.Request(tcp.data)

# examine the attributes

print(http.method)
# GET
print(http.uri)
# /testurl
print(http.version)
# 1.1
print(http.headers['user-agent'])
# Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.5)


################## Full Script ##########################

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