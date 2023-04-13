#!/usr/bin/python3
"""A module that reads stdin line by line and computes metrics"""

import sys

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
total_size = 0
status_count = {code: 0 for code in status_codes}


def print_stats():
    """Prints the statistics"""
    print("File size: {}".format(total_size))
    for code in status_codes:
        if status_count[code] > 0:
            print("{}: {}".format(code, status_count[code]))


try:
    for i, line in enumerate(sys.stdin, 1):
        tokens = line.split()
        if len(tokens) > 2:
            size = int(tokens[-1])
            status = int(tokens[-2])
            total_size += size
            if status in status_codes:
                status_count[status] += 1
        if i % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
print_stats()
