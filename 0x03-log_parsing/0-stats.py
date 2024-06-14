#!/usr/bin/python3
import sys
import signal


total_size = 0
status_counts = {code: 0 for code in ['200',
'301', '400', '401', '403', '404', '405', '500']}
line_count = 0


def print_stats():
    """ Print the current statistics. """
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")


def signal_handler(sig, frame):
    """ Handle the keyboard interrupt signal (CTRL + C). """
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


def process_line(line):
    global total_size, line_count
    try:
        parts = line.split()
        if len(parts) < 9:
            return

        status_code = parts[-2]
        file_size = parts[-1]

        if status_code in status_counts:
            status_counts[status_code] += 1

        total_size += int(file_size)

        line_count += 1

        if line_count % 10 == 0:
            print_stats()

    except Exception as e:
        pass

for line in sys.stdin:
    process_line(line)

print_stats()
