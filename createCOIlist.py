# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 10:27:41 2021

@author: jholland
"""
import bibtexparser

with open('Q:\\My Drive\\grants\\COI\\JBHworks_03182021.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

#print(bib_database.entries)

#define the publication years that we want to report co-authors from
#in this case, it means go back to year 2017 (it's usually five years to make sure we get complete set of four years going back)
currentYear = 2021
goBack = 4
years = [str(i) for i in list(range(currentYear - goBack, currentYear + 1))]


def reformatAuthors(authorGroup):
    #Takes in a single string as authorGroup, splits into individual author names
    #returns a list with author names formatted as Last, First, rest
    current_authors = authorGroup.split(' and ')#split the string of all the names
    names = [] #make an empty list to put the parsed names into
    for author in current_authors:
        if author.find(',') >= 0: #if there is a comma, format is OK as is
            names.append(author)
        else:
            authorSplit = author.split(' ')
            newname = authorSplit.pop() #pop last name out of list
            newname = newname + ', ' + authorSplit.pop(0) #join last, comma, first
            newname = newname + ' ' + ' '.join(authorSplit) # add the remaining names or initials separate by spaces
            names.append(newname)
    return(names)


authorList = []

for paper in bib_database.entries:
    if paper['year'] in years:
        current_group = paper['author']
        authors = reformatAuthors(current_group)
        for author in authors:
            if author not in authorList:
                authorList.append(author)
    else: pass #if the paper is not within the range of years desired, pass over it
    
#sort the complete list alphabetically
authorList.sort()

#write the list out to a txt file
with open('Q:\\My Drive\\grants\\COI\\COI_author_list.txt', 'w') as f:
    f.write('\n'.join(authorList))
        
        