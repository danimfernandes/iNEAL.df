#!/usr/bin/python3

__author__ = 'daniel'

import sys
import os

print("< CONVERTINGIT - Wrapper to quickly convert a dataset with 'convertf' >\n")

## Description and Usage ##
helpa = """
    # Description and Usage #
    > 1. Description
    Quickly convert a dataset to a desired format accepted by 'convertf' from the 'admixtools' package.
    This wrapper script creates the parameter file using default options and uses the 'outputformat' given as an argument.

    > 2. Requirements
    Python modules:
        -os
        -sys

    > 3. Usage
    Input:
    convertingit.py fooDataset inputFormat outputFormat

    Output:
    fooDatasetReduced.geno/bed
    fooDatasetReduced.snp/bim
    fooDatasetReduced.ind/fam

    Example:
    >>> convertingit.py myDataset1 PACKEDPED EIGENSTRAT
    """

cwd = os.getcwd()
    ## Command-line argument and general error checking ##
comLen = len(sys.argv)
if comLen == 2 and sys.argv[1] == "-h":
    print(helpa)
    quit()
if comLen == 1 or comLen == 2:
    print("\t> ERROR: Three command-line arguments are needed. Type 'convertingit.py -h' for help.")
    quit()
if comLen > 4:
    print("\t> ERROR: Only three command-line arguments are needed. Type 'convertingit.py -h' for help.")
    quit()
elif comLen == 2:
    print("\t> ERROR: Three command-line arguments are needed. Type 'convertingit.py -h' for help.")
datasetIn=sys.argv[1]
inputFormat=sys.argv[2]
outputFormat=sys.argv[3]

if outputFormat == "PACKEDANCESTRYMAP":
	datasetOut = datasetIn + "_PAM"
###new
elif outputFormat == "EIGENSTRAT" and inputFormat == "PACKEDANCESTRYMAP" and datasetIn[-4:] == "_PAM":
	datasetOut = datasetIn + "_EIG"
###endnew

else:
	datasetOut = datasetIn

print("\tDataset In: " + datasetIn)
print("\tInput Format: " + inputFormat)
print("\tDataset Out: " + datasetOut)
print("\tOutput Format: " + outputFormat)

if inputFormat == "PACKEDPED":
	ext1in = ".bed"
	ext2in = ".bim"
	ext3in = ".fam"
if inputFormat == "PED":
	ext1in = ".ped"
	ext2in = ".map"
	ext3in = ".ped"
if inputFormat == "PACKEDANCESTRYMAP" or inputFormat == "ANCESTRYMAP" or inputFormat == "EIGENSTRAT":
	ext1in = ".geno"
	ext2in = ".snp"
	ext3in = ".ind"

if outputFormat == "PACKEDPED":
	ext1out = ".bed"
	ext2out = ".bim"
	ext3out = ".fam"
if outputFormat == "PED":
	ext1out = ".ped"
	ext2out = ".map"
	ext3out = ".ped"
if outputFormat == "PACKEDANCESTRYMAP" or outputFormat == "ANCESTRYMAP" or outputFormat == "EIGENSTRAT":
	ext1out = ".geno"
	ext2out = ".snp"
	ext3out = ".ind"

if inputFormat == "PACKEDPED" or inputFormat == "PED" and outputFormat == "PACKEDANCESTRYMAP":
	fout = open('CONV', 'w')
	fout.write("genotypename: " + datasetIn + ext1in + "\nsnpname: " + datasetIn + ext2in + "\nindivname: " + datasetIn + ext3in + "\noutputformat:	EIGENSTRAT\n")
	fout.write("genotypeoutname: " + datasetIn + ext1out + "\nsnpoutname: " + datasetIn + ext2out + "\nindivoutname: " + datasetIn + ext3out + "\nfamilynames: YES")

	fout.close()

	os.system("convertf -p CONV > /dev/null")
	os.system("indfile_correction.py")

	fout = open('CONV', 'w')

	fout.write("genotypename: " + datasetIn + ext1out + "\nsnpname: " + datasetIn + ext2out + "\nindivname: " + datasetIn + ext3out + "\noutputformat:	" + outputFormat + "\n")
	fout.write("genotypeoutname: " + datasetOut + ext1out + "\nsnpoutname: " + datasetOut + ext2out + "\nindivoutname: " + datasetOut + ext3out + "\nfamilynames: YES")

	fout.close()

	os.system("convertf -p CONV > /dev/null")

else:
	fout = open('CONV', 'w')
	fout.write("genotypename: " + datasetIn + ext1in + "\nsnpname: " + datasetIn + ext2in + "\nindivname: " + datasetIn + ext3in + "\noutputformat:	" + outputFormat + "\n")
	fout.write("genotypeoutname: " + datasetOut + ext1out + "\nsnpoutname: " + datasetOut + ext2out + "\nindivoutname: " + datasetOut + ext3out + "\nfamilynames: YES")

	fout.close()

	os.system("convertf -p CONV > /dev/null")

if inputFormat == "PACKEDANCESTRYMAP" or inputFormat == "ANCESTRYMAP" or inputFormat == "EIGENSTRAT":
	if outputFormat == "PACKEDPED":
		os.system("famfile_correction.py")

if inputFormat == "PACKEDPED":
	if outputFormat == "ANCESTRYMAP" or outputFormat == "EIGENSTRAT":
		os.system("indfile_correction.py")

fout.close()