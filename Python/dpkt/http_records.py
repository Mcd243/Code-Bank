 
 
 # extract HTTP requests sent to a Web server (i.e. records with a destination port of 80).
 dpkt.http.Request()

#  extract the 'method' values from the HTTP record
print(f'{repr(http.method)}')

# extract the 'refer' values from HTTP.headers
print(f'{repr(http.headers[“referrer”])}') – as referrer dict key

# The following lines of code will print the HTTP record.

if tcp.dport == 80:
    http = dpkt.http.Request(tcp.data)
    print(f"#<INFO> HTTP request: {repr(http)}")

# The HTTP record has four attributes: version, method, uri and headers.
# http.version, http.method, http.uri and http.headers (headers is a OrderedDic)
#One of its keys is ‘referer’, therefore the associated values can be found using http.headers['referer'] 


import socket, dpkt
from parse_pcap import main

packets = main(print_out=False, break_first=False)
#print(packets[0])

## Insert code here
for p in packets:
        ip = p.data
        tcp = ip.data
        print(f"Connection details: {socket.inet_ntoa(ip.src)}:{tcp.sport} -> {socket.inet_ntoa(ip.dst)}:{tcp.dport}")
        
        if tcp.dport == 80:
            try:
                http = dpkt.http.Request(tcp.data)
                #print(f"#<INFO> HTTP request: {repr(http)}")
                print("HTTP INFO")
                print(f"# method: {http.method}")
                print(f"# referrer: {http.headers['referer']}")
            except:
                print(f"#<INFO> HTTP parsing error")
        print("\n")
