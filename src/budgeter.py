#!/usr/bin/env python3

import argparse

from pathlib import Path

def parse_arguments():
    parser = argparse.ArgumentParser(description="Automatically buckets expenses into a budge tracker")
    parser.add_argument("--budget-directories", required=True, help="Directory where your budget sheet is found", type=Path)
    # TODO - Parse this from a string rather than an int. Can be taken as general clean up after pdf parsing.
    parser.add_argument("--month", required=True,  help="The month you want to work on", type=int)
    return parser.parse_args()

def main(args) -> None:
    print("Hello World!")

if __name__ == "__main__":
    arguments = parse_arguments()
    main(arguments)
