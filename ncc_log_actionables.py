# region headers
# Parser for ncc logs
# * author:     manoj.mone@nutanix.com
# * version:    2020/06/04, v1
# file_name:    ncc_log_actionables
# description:  Given a ncc log file, search all lines that list Errors, Failures and Warnings
# endregion

import os
import re

infile = input("Please enter the ncc log file name:")

important = []
keep_phrases = ["FAIL:",
              "ERR :",
              "WARN:"]

# Output file, where the matched loglines will be copied to
output_filename = os.path.normpath("parsed_lines_that_need_attention.log")


with open(output_filename, "w") as out_file:
    out_file.write("")

# Open output file in 'append' mode
with open(output_filename, "a") as out_file:
    # Open input file in 'read' mode
    with open(infile, "r") as in_file:
        # Loop over each log line
        for line in in_file:
            # If log line matches our regex, print to console, and output file
            for phrase in keep_phrases:
                if phrase in line:
                    to_report = phrase
                    if to_report.startswith('FAIL:') or to_report.startswith('ERR :') or to_report.startswith('WARN:'):
                        print (line)
                        out_file.write(line)
