#!/usr/bin/env python3

import argparse
import sys
import re

def check_numeric_filenames(filenames):
    numeric_file_pattern = re.compile(r"^[0-9]+\.py$")
    errors = False
    for filename in filenames:
        if numeric_file_pattern.match(filename):
            print(f"Error: Found a python file with a numeric name ({filename}).")
            errors = True
    return errors

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to check.")
    args = parser.parse_args()

    if check_numeric_filenames(args.filenames):
        sys.exit(1)

if __name__ == "__main__":
    main()

