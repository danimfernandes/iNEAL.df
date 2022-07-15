#!/usr/bin/python3

__author__ = 'daniel'

import sys
import os

print("< REDUCINGIT - Wrapper to quickly reduce a dataset with 'convertf' >\n")

## Description and Usage ##
helpa = """
    # Description and Usage #
    > 1. Description
    Quickly reduce a dataset in EIGENSTRAT or [PACKED]ANCESTRYMAP formats using 'convertf' from the 'admixtools' package given a list of populations to keep.
    This wrapper script creates the parameter file using default options and uses the 'poplistname' given as an argument.

    > 2. Requirements
    Python modules:
        -os
        -sys

    > 3. Usage
    Input:
    reducingit.py fooDataset poplistnameFile fooDatasetReduced

    Output:
    fooDatasetReduced.geno
    fooDatasetReduced.snp
    fooDatasetReduced.ind

    Example:
    >>> reducingit.py myDataset1 keep_myPopList myDataset1_reduced
    """

cwd = os.getcwd()
    ## Command-line argument and general error checking ##
comLen = len(sys.argv)
if comLen == 1 or comLen == 3:
    print("\t> ERROR: Three command-line arguments are needed. Type '{} -h' for help.")
    quit()
if comLen > 4:
    print("\t> ERROR: Only three command-line arguments are needed. Type '{} -h' for help.")
    quit()
if comLen == 2 and sys.argv[1] == "-h":
    print(helpa)
    quit()
elif comLen == 2:
    print("\t> ERROR: Three command-line arguments are needed. Type '{} -h' for help.")
dataset=sys.argv[1]
poplist=sys.argv[2]
reducedDataset=sys.argv[3]

print("\tDataset: " + dataset)
print("\tPoplistFile: " + poplist)
print("\tReduced Dataset: " + reducedDataset + "\n")

fout = open('CONV_REDUCE', 'w')

fout.write("genotypename: " + dataset + ".geno\nsnpname: " + dataset + ".snp\nindivname: " + dataset + ".ind\noutputformat:	PACKEDANCESTRYMAP\ngenotypeoutname: " + reducedDataset + ".geno\nsnpoutname: " + reducedDataset + ".snp\nindivoutname: " + reducedDataset + ".ind\npoplistname: " + poplist)

fout.close()

os.system("convertf -p CONV_REDUCE > /dev/null")