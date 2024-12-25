def openFile(data, file):
    with open(file, "r") as db:
        # Read all lines and strip any extraneous newline characters or empty lines
        x = db.readlines()

    # Ensure we only append valid lines
    for line in x:
        # Strip leading/trailing whitespace (including newlines) from each line
        stripped_line = line.strip()
        if stripped_line:  # Only add non-empty lines
            data.append(stripped_line)
