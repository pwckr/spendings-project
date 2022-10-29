def import_text_file(input):
    with open(input) as text:
        rows = text.readlines()

    return rows