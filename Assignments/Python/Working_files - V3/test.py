# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 14:00:43 2021

@author: RickyP
"""
import socket
import dpkt
import re


def find_in_pcap(pcap):
    '''in current form, finds any gif files downloaded and prints
       request source (Downloader), gif URI and destination (provider) IP'''

    found = False
    for (time_s, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip_ad = eth.data
            src = socket.inet_ntoa(ip_ad.src)
            dst = socket.inet_ntoa(ip_ad.dst)
            tcp = ip.data

            http = dpkt.http.Request(tcp.data)
            if http.method == 'GET':
                uri = http.uri.lower()
                match = re.search(r"^*.gif$", uri)
                if match in uri:
                    print(f'[!] {src} downloaded {uri} from {dst}')
                    found = True
        except Exception:
            # necessary as many packets would otherwise generate an error
            pass
    return found


def main():
    # should get results with filtered2.pcap but none with filtered3.pcap
    pcap_file = "filtered2.pcap"
    f = open(pcap_file, 'rb')
    pcap = dpkt.pcap.Reader(f)

    print(f'[*] Analysing {pcap_file} for gif files')
    # call find_download which prints results
    result = find_download(pcap)
    if result is False:
        print('No gif downloads found in this file')


if __name__ == '__main__':
    main()
