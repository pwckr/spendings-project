import globals
import read_data
import re

rows = read_data.import_text_file(globals.TEXT)

def prune_unnecessary_rows(rows):
    # rows to remove: 0, 1
    rows = rows[2:]
    return rows

def check_for_msg_head(line):
    if line[0] == "[" and line[19] == "]":
        timestamp = line[:20]
        user, body = extract_user_and_body(line[21:])
        return [True, timestamp, user, body]
    else:
        return [False, line[:-2]]

def extract_user_and_body(line_without_timestamp):
    i =0
    for char in line_without_timestamp:
        if char ==":":
            return line_without_timestamp[:i], line_without_timestamp[i+2:-1]
        i += 1
    return None

rows = prune_unnecessary_rows(rows)