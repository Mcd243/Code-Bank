"""
Created on Wed Oct 27 15:31:35 2021

@author: Muun Macdonald
"""
import sys
from datetime import datetime
from prettytable import PrettyTable


def mean_p_len(data_list):
    """ A function to determine the mean length of packet"""
    total_len = 0
    try:
        for item in data_list:
            total_len += item[1]
        mean_len = total_len / len(data_list)
        return round(mean_len, 2)
    except TypeError as err:
        print(f"!! Input is the wrong type ({err.__class__.__name__}) : "
              f"{err}", file=sys.stderr)
    except Exception as err:
        print(f"!! Exception ({err.__class__.__name__}) : {err}",
              file=sys.stderr)


def ts_convert(timestamp):
    """ A function to convert a timestamp to a datetime object."""
    try:
        # https://stackoverflow.com/questions/3682748/converting-unix-
        # timestamp-string-to-readable-date
        # Daniel F
        # Dec 23 '20 at 6:18
        d_t = datetime.fromtimestamp(timestamp)
        rezolved_dt: str = f"{d_t:%Y-%m-%d %H:%M:%S}"
        return rezolved_dt
    except TypeError as err:
        print(f"!! Input is the wrong type ({err.__class__.__name__}) : {err}",
              file=sys.stderr)
    except Exception as err:
        print(f"!! Exception ({err.__class__.__name__}) : {err}", file=sys.stderr)


def summary_table(summary_data):
    """Create a summary table of the parsed pcap files and return the table."""
    try:
        # https://www.geeksforgeeks.org/how-to-make-a-table-in-python/
        # khushali_verma
        #  18 Aug, 2020
        summary = PrettyTable(
            ["Protocol", "Number of Packets", "First Timestamp", "Last Timestamp",
             "Mean Packet Length"])
        for key in summary_data:
            summary.add_row(
                [key, len(summary_data[key]), ts_convert(summary_data[key][0][0]),
                 ts_convert(summary_data[key][-1][0]),
                 mean_p_len(summary_data[key])])
        return summary
    except ImportError as err:
        print(f"!! Import problem({err.__class__.__name__}) : {err}", file=sys.stderr)
    except TypeError as err:
        print(f"!! Input is the wrong type ({err.__class__.__name__}) : {err}", file=sys.stderr)
    except Exception as err:
        print(f"!! Exception ({err.__class__.__name__}) : {err}", file=sys.stderr)


if __name__ == "__main__":
    summary_table()
