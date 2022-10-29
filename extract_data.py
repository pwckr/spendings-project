import globals
import read_data

rows = read_data.import_text_file(globals.TEXT)

def prune_unnecessary_rows(rows):
    # rows to remove: 0, 1
    rows = rows[2:]
    return rows