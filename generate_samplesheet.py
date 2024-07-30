#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 09:17:46 2023

@author: Vinícius Rodovalho
"""

import re
import sys
import os
import pandas as pd
from pathlib import Path
import argparse

def absoluteFilePaths(directory, extension="*.fastq.gz"):
    '''
    Find all files ending with extension in directory and subdirectories.
    '''
    result = list(Path(directory).rglob(extension))
    return result

def get_details_from_file_paths(file_paths,  paired=False, file_name_pattern='([a-zA-Z_]+).effective(.fastq.gz)',
                                extension="*.fastq.gz", replace_pairs=("R1", "R2")):
    '''
    Get files IDs, forward and reverse complete paths.
    '''
    details = {}
    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        file_path = str(file_path).replace('\\', '/')

        matched = re.match(pattern=file_name_pattern, string=file_name)

        if matched:
            file_id = matched.group(1)
            print(f"Found {file_id} in {file_path}...")

            if file_id not in details:
                details[file_id] = {'sampleID' : file_id}
                forward = str(file_path)
                if paired.upper() == "TRUE":
                    item1, item2 = replace_pairs.split(',')
                    reverse = forward.replace(item1, item2)
                    reverse_path = Path(reverse)
                    if not reverse_path.is_file():
                        print(f"\n>> Warning: file {reverse} not found...\n")
                    details[file_id]['forwardReads'] = forward
                    details[file_id]['reverseReads'] = reverse
                else:
                    details[file_id]['forwardReads'] = forward
    return details

def organize_list_of_files(directory, paired=False, file_name_pattern='([a-zA-Z_]+).effective(.fastq.gz)',
                           replace_pairs="R1,R2"):
    '''
    '''
    # prepare for df creation based on single or paired-end reads
    base_cols = ["sampleID"]
    if paired.upper() == "TRUE":
        columns = base_cols + ["forwardReads", "reverseReads"]
        second_row = ["#q2:types"] + ["categorical"] * 2
    else:
        columns = base_cols + ["forwardReads"]
        second_row = ["#q2:types"] + ["categorical"] * 1
    
    # construct df with 1st row
    df = pd.DataFrame(columns=columns)
    
    # get files paths
    extension = "*" + re.match(pattern=".*\((.*)\)", string=file_name_pattern).group(1)
    files_paths = absoluteFilePaths(directory, extension=extension)
    
    # get details
    details = get_details_from_file_paths(
        files_paths,  
        paired=paired, 
        file_name_pattern=file_name_pattern, 
        extension=extension,
        replace_pairs=replace_pairs)
    details_df = pd.DataFrame(details).T
    
    # concatenate details
    df = pd.concat([df, details_df])
    df = df.sort_values(by=["sampleID"], ascending=True)    
    return df

# Create the parser
parser = argparse.ArgumentParser()
# Add arguments
parser.add_argument('--input', type=str, required=True, help='The input directory. Use full file paths, not relative ones!')
parser.add_argument('--pattern', type=str, required=True, 
                    help='''File name regex pattern. 
                    Parenthesis should enclose both (sample name) and (file extension).
                    Parts of the file name that do not belong to sample ID or file extension should be out of parenthesis.
                    Example for single-end reads: "([a-zA-Z0-9_]+).effective(.fastq.gz)", 
                    Example for paired-end reads: "([a-zA-Z0-9_]+).*R1.*(.fastq.gz)"''')
parser.add_argument('--paired', type=str, required=False, default=False, help='Paired-end sequences? True or False. Default: False')
parser.add_argument('--replace', type=str, required=False, default="R1,R2", help='Replace pair for paired-end reads, separated by comma. Default: R1,R2')
parser.add_argument('--output', type=str, required=False, default="samplesheet.tsv", help='The output tsv file. Default: samplesheet.tsv')

try:
    args = parser.parse_args()
    #print(f"Running the script with the parameters: {args}\n")
    result = organize_list_of_files(directory=args.input, 
                                    paired=args.paired, 
                                    file_name_pattern=args.pattern,
                                    replace_pairs=args.replace)
    print(f"Saving result to: {args.output}")
    result.to_csv(args.output, index=False, sep='\t')
except Exception as e: 
    parser.print_help()
    print('\n# Example (single): generate_samplesheet.py --input data --pattern "([a-zA-Z0-9_]+).*effective.*(.fastq.gz)" --paired False')
    print('# Example (paired): generate_samplesheet.py --input data --pattern "([a-zA-Z0-9_]+)_xxx.*R1.*(.fastq.gz)" --paired True --replace R1,R2')
    print(f"\nError: {e}\n")
    sys.exit(0)
