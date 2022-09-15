"""
Created on Wed Oct 27 15:31:35 2021

@author: Muun Macdonald
"""
import sys
import matplotlib.pyplot as plt
from datetime import datetime

def ts_convert(timestamp) -> str:
    """ A function to convert a timestamp to a datetime object."""
    # https://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date
    # Daniel F
    # Dec 23 '20 at 6:18
    dt = datetime.fromtimestamp(timestamp)
    resolved_dt: str = f"{dt:%H:%M:%S}"
    return resolved_dt


def pcap_stats(timestamp):
    """A function to group timestamps into time periods and count the timestamps in that each grouping. The function
    returns time as a x-axis and number of timestamps as a y-axis for the plotting of a graph."""
    timestamp_list = []
    inner_list = []
    no_packets_list = []
    first_timestamp = []
    hr_timestamp = []
    time_grouping = 10
    time_grouping = int(input("Enter a time grouping number to display plot the graph. 10 is recommended."))
    first = timestamp[0]
    last = timestamp[0] + time_grouping

    # If the time in the time interval add the time to a list
    for time in timestamp:
        if first <= time < last:
            inner_list.append(time)
        # If the time is greater than the time interval
        elif time > last:
            timestamp_list.append(inner_list)
            if len(inner_list) > 0:
                first_timestamp.append(inner_list[0])
                no_packets_list.append(len(inner_list))
            inner_list = []
            first = last
            last += time_grouping
    for time in first_timestamp:
        hr_timestamp.append(ts_convert(time))
    return hr_timestamp, no_packets_list


def stats(timestamps):
    """ This function plots a graph from timestamp data."""
    try:
        # https://datatofish.com/line-chart-python-matplotlib/
        # April 12, 2020
        x_list, y_list = pcap_stats(timestamps)
        plt.plot(x_list, y_list, color='green', marker='o')
        plt.plot()
        plt.title('Number of Packets Vs Time', fontsize=12)
        plt.xlabel('Time', fontsize=12)
        plt.ylabel('Number of Packets', fontsize=12)
        stat_plot = plt.show()
        return stat_plot
    except ImportError as err:
        print(f"!! Import problem({err.__class__.__name__}) : {err}", file=sys.stderr)


if __name__ == "__main__":
    stats()
