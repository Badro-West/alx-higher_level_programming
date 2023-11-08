#!/usr/bin/python3
import sys

def print_stats(file_sizes, status_codes):
    print("File size: {}".format(sum(file_sizes)))
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

file_sizes = []
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            file_size = int(parts[-1])
            status_code = int(parts[-2])

            file_sizes.append(file_size)
            status_codes[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_stats(file_sizes, status_codes)

        except (ValueError, IndexError):
            pass

except KeyboardInterrupt:
    pass

print_stats(file_sizes, status_codes)

