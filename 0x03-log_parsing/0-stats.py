#!/usr/bin/python3
""" A script that reads stdin line by line and computes metrics """
import sys
import signal


total_size = 0
status_counts = {}
valid_status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
line_count = 0


def print_stats():
    """ Print the current statistics. """
    print(f"File size: {total_size}")
    for status in sorted(status_counts):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")


def signal_handler(sig, frame):
    """ Handle the keyboard interrupt signal (CTRL + C). """
    print_stats()
    sys.exit(0)

# Set up the signal handler for keyboard interrupt (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

# Read from stdin
for line in sys.stdin:
    line_count += 1
    try:
        parts = line.split()
        if len(parts) != 10:
            continue

        # Extract status code and file size
        status_code = parts[-2]
        file_size = parts[-1]

        if status_code in valid_status_codes:
            if status_code not in status_counts:
                status_counts[status_code] = 0
            status_counts[status_code] += 1

        total_size += int(file_size)

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_stats()

    except Exception as e:
        continue


# If the script ends normally (EOF), print the statistics
print_stats()
