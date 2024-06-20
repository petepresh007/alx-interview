#!/usr/bin/python3
'''module for stat'''
import sys
import signal
import re


total_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0


def print_stats():
    """ Print the computed metrics. """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    """ Handle keyboard interruption. """
    print_stats()
    sys.exit(0)


# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

log_line_pattern = re.compile(
    r'^(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\] '
    r'"GET /projects/260 HTTP/1.1" (\d+) (\d+)$'
)

try:
    for line in sys.stdin:
        match = log_line_pattern.match(line.strip())
        if match:
            ip, date, status_code, file_size = match.groups()
            file_size = int(file_size)
            if status_code in status_codes:
                status_codes[status_code] += 1
            total_size += file_size
            line_count += 1

            if line_count % 10 == 0:
                print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

# Print remaining stats if any
print_stats()
