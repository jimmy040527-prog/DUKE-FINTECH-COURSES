import sys
from sys import argv


def read_key_values(filename):
    """
    Reads a key-value delimited file (separated by first =) into a dictionary

    Args:
    filename(str): name of the file to read
    
    Returns:
    dictionary of the read items
    """
    key_values = {}

    with open(filename, "r") as file:
        for line in file:
            key, value = line.strip().split('=', 1)
            key_values[key] = value
    return key_values


def create_output_filename(name):
    """
    create the output file name.  Given an input filename such as "input.txt",
    return "input.txt.counts"
    """
    return name + ".counts"


def process_key_file(filename, key_values):
    """
    Loads in a key file and produces a dictionary of the count of the values 
    If a key is not found in key_values use "<unknown>"

    Args:
    filename(str): file containing keys to process
    key_values(dict): existing keys to load
    """
    counts = {}

    with open(filename, "r") as file:
        for line in file:
            key = line.strip()
            value = key_values.get(key, '<unknown>')
            counts[value] = counts.get(value, 0) + 1
            
    return counts


def write_output(filename, counts):
    """
    Writes the content of counts to a file specifed by the filename.
    The output order is by the highest count descending. If two values are
    equal, arbitrarily choose 1.
    For each line, the format is
      key: value
    

    Args:
    filename(str): filename to open and write the output to.
    counts(dict): existing keys to load   
    Returns: None 
    """
    with open(filename, "w") as file:
        for key in sorted(counts, key=counts.get, reverse=True):
            file.write(f"{key}: {counts[key]}\n")


def process(args):
    """
    Implement your algorithm in this function
    """
    # print(args)   #Uncomment if you want to validate/see the command-line arguments
    key_values = read_key_values(args[1])

    for filename in args[2:]:
        counts = process_key_file(filename, key_values)
        output_filename = create_output_filename(filename)
        write_output(output_filename, counts)


# __name__ == "__main__" and argv explained in the "modules" notebook
if __name__ == "__main__":
    if len(argv) < 3:
        print("Usage: python3 key_value.py file1_name file2_name ...")
        sys.exit(-1)
    process(argv)
