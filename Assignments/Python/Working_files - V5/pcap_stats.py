"""
Created on Wed Oct 27 15:31:35 2021

@author: RickyP
"""

import matplotlib.pyplot as plt

def pcap_stats(timestamp):
    """Sum stuff"""
    first = timestamp[0]
    last = timestamp[0]
    timestamp_list = []
    inner_list = []
    no_packets_list = []
    first_timestamp = []
    time_grouping = 10
    default = timestamp[0]
    first = timestamp[0]
    last = timestamp[0] + time_grouping

    for time in timestamp:
        if first <= time < last:
            inner_list.append(time)
        elif time > last:
            if len(inner_list) == 0:
                inner_list.append(default)
            else:
                first_timestamp.append(inner_list[0])
            timestamp_list.append(inner_list)
            no_packets_list.append(len(inner_list))
            inner_list = []
            first = last
            last += time_grouping
    print(no_packets_list)
    print(first_timestamp)
    print(len(no_packets_list))
    print(len(first_timestamp))
    return first_timestamp, no_packets_list


def stats(timestamps):
    x_list, y_list = pcap_stats(timestamps)
    plt.plot(x_list, y_list, color='red', marker='o')
    plt.title('Number of Packets Vs Time', fontsize=14)
    plt.xlabel('Time', fontsize=14)
    plt.ylabel('Number of Packets', fontsize=14)
    plt.grid(True)
    stat_plot = plt.show()
    return stat_plot


if __name__ == "__main__":
    stats()