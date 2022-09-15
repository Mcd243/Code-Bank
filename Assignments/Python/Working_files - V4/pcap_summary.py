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
    # Contango
    dt = datetime.fromtimestamp(timestamp)
    rezolved_dt: str = f"{dt:%Y-%m-%d %H:%M:%S}"
    return rezolved_dt


def summary_table(summary_data):
    """Sun stuff"""
    # Create a summary table of the parsed pcap files
    # https://www.geeksforgeeks.org/how-to-make-a-table-in-python/
    summary = PrettyTable(
        ["Student Name", "Number of Packets", "First Timestamp", "Last Timestamp", "Mean Packet Length"])
    if len(summary_data[0]) > 0:
        summary.add_row(
            ["TCP", len(summary_data[0]), ts_convert(summary_data[0][0][0]), ts_convert(summary_data[0][-1][0]),
             mean_p_len(summary_data[0])])
    if len(summary_data[1]) > 0:
        summary.add_row(
            ["UDP", len(summary_data[1]), ts_convert(summary_data[1][0][0]), ts_convert(summary_data[1][-1][0]),
             mean_p_len(summary_data[1])])
    if len(summary_data[2]) > 0:
        summary.add_row(
            ["IGMP", len(summary_data[2]), ts_convert(summary_data[2][0][0]), ts_convert(summary_data[2][-1][0]),
             mean_p_len(summary_data[2])])
    if len(summary_data[3]) > 0:
        summary.add_row(["OTHER", len(summary_data[3]), ts_convert(summary_data[3][0][0]),
                         ts_convert(summary_data[3][-1][0]), mean_p_len(summary_data[3])])
    return summary


if __name__ == "__main__":
    summary_table()