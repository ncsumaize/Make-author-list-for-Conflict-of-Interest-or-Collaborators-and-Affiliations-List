# -*- coding: utf-8 -*-
"""
Create Collaborators and Other Affiliations List of Co-Authors for NSF proposal

From Scholar Google profile page, sort by year, and select all papers going back 48 months
Export as RefMan format, download the resulting citations.ris file
"""

import os
import re
os.chdir("C:/Users/jholland/Downloads")

fname = "citations.ris"

with open(fname) as file:
    lines = [line.strip() for line in file]


#extract the lines that start with 'A1' - these are co-authors
lines2 = [x for x in lines if x[0:2] == "A1" ]

#strip of the prefix stuff and any trailing stuff
prefx = re.compile(r"^A1\s+-\s+", re.IGNORECASE) 
re.sub(prefx, "", lines2[0]).strip() 

lines2 = [re.sub(prefx, "", x).strip() for x in lines2]

#sort the authors
authors = sorted(lines2)

#remove duplicates
authors_unique = list(dict.fromkeys(authors))

#This only removes exact duplicates, it will be be more work to remove individuals differing only by middle name, for example

#write lines2 to a text file

with open('references.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % x for x in authors_unique)