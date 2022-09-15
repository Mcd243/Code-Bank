"""
Created on Wed Oct 27 15:31:35 2021

@author: RickyP
"""


from prettytable import PrettyTable
from datetime import datetime


def mean_p_len(data_list) -> float:
    """ A function to determine the mean length of packet"""
    total_len = 0
    for item in data_list:
        total_len += item[1]
    mean_len = total_len / len(data_list)
    return round(mean_len, 2)


def ts_convert(timestamp) -> str:
    """ A function to convert a timestamp to a datetime object."""
    # https://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date
    # Daniel F
    # Dec 23 '20 at 6:18
    dt = datetime.fromtimestamp(timestamp)
    rezolved_dt: str = f"{dt:%Y-%m-%d %H:%M:%S}"
    return rezolved_dt


def summary_table(summary_data):
    """Create a summary table of the parsed pcap files"""
    # https://www.geeksforgeeks.org/how-to-make-a-table-in-python/
    # khushali_verma
    #  18 Aug, 2020
    summary = PrettyTable(
        ["Protocol", "Number of Packets", "First Timestamp", "Last Timestamp", "Mean Packet Length"])
    for key in summary_data:
        summary.add_row(
            [key, len(summary_data[key]), ts_convert(summary_data[key][0][0]), ts_convert(summary_data[key][-1][0]), mean_p_len(summary_data[key])])
    return summary


if __name__ == "__main__":
    summary_table()
