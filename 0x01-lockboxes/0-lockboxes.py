#!/usr/bin/python3
""" Lockboxes problem. """


def canUnlockAll(boxes):
    """    This function determines if all boxes can be opened.    """
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
            elif box >= len(boxes):
                return False
    if len(keys) == len(boxes):
        return True
    return False
