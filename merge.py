#!/usr/bin/env python3
import sys
import argparse
import os
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

parser = argparse.ArgumentParser(description='PDFbot x3000. ')

parser.add_argument('-i','--input', nargs='+', help='files to input', required=True)
parser.add_argument('-o','--output',help='output file name', required=True)


def die(msg):
    print(msg)
    exit(0)

def verify_input_file_exists(list_of_files):
    for f in list_of_files:
        if not os.path.exists(f):
            die("File " + f + " does not exist. Exiting...")

def verify_output_file_not_exist(output):
    if os.path.exists(output):
        choice = input("Output file exists... Overwrite? (y/n)  ")
        if choice.lower() == "y":
            return True
        else:
            die("Please supply a unique file name. Aborting...")

def merge_files(list_of_files, output_file):
    verify_input_file_exists(list_of_files)
    verify_output_file_not_exist(output_file)
    merger = PdfFileMerger()
    
    print("Merging files")
    for filename in list_of_files:
        print("-> " + filename)
        merger.append(PdfFileReader(open(filename, 'rb')))
    print("Merged to file " + output_file)
    merger.write(output_file)


if __name__ == "__main__":
    args = parser.parse_args()  
    if not args.input:
        die("ERROR: No input file(s) specified.")
    if not args.output:
        die("ERROR: No output file specified.")

    merge_files(args.input, args.output)

