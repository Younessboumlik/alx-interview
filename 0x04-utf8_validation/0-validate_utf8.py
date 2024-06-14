#!/usr/bin/python3
""" Check if a given data set represents a valid UTF-8 encoding. """


def validUTF8(data):
    """
    Method to determine if a given dataset represents a valid UTF-8 encoding.
    """

    number_of_bytes = 0

    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        mask = 1 << 7
        if number_of_bytes == 0:
            # Count the number of leading 1's
            while mask & byte:
                number_of_bytes += 1
                mask = mask >> 1

            if number_of_bytes == 0:
                continue

            if number_of_bytes == 1 or number_of_bytes > 4:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False

        number_of_bytes -= 1

    return number_of_bytes == 0
