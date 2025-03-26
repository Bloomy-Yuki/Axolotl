import pandas as pd
'''
this file converts .md files written in Axolotl-standard into
Anki deck format .csv file.
-------------------------------------
V 0.1:
23.03.2025
- Added support for all kinds of notes, including texts and anything else really.
-------------------------------------
the Axolotl-standard:

## Chapter_name

1. Card_face $LaTeX_code$ :

$$
LaTeX_code
$$
$$
LaTeX_code
$$

2. Card_face $LaTeX_code$ :
$$
LaTeX_code
$$

## Chapter_name

3. Card_face:
$$
LaTeX_code
$
...
-------------------------------------

Things to look out for:

1. dont have both "." and ":" in any line except card faces
2. dont have "##" except in chapter_name

-------------------------------------
25.01.2025
'''
# Loading the File & preparing empty data variable:
File_name = input("Enter file name:")
global Data
Data = [[],[],[]]
with open(File_name + ".md", encoding='utf-8') as file:
    lines = [line.rstrip() for line in file]
     
# 1. getting the right format:

#----------------------------------------------

    # replacing double moneysigns:
def replace_double_money(lines):
    n = 0    
    for line in range(0,len(lines)):

        for i in range(0,len(lines[line]) - 1):

            if  lines[line][i:i + 2] == '$$':
                if n == 0:
                    lines[line] = lines[line].replace("$","\\",1)
                    lines[line] = lines[line].replace("$","[",1)
                    n = 1
                else: 
                    n == 1
                    lines[line] = lines[line].replace("$","\\",1)
                    lines[line] = lines[line].replace("$","]",1)
                    n = 0

#----------------------------------------------

    # replacing single moneysigns:
def replace_single_money(lines):
    n = 0
    
    for line in range(0,len(lines)):

        for lett in lines[line]:

            if (lett == '$') and (n % 2 == 0):
                    lines[line] = lines[line].replace("$","\\(",1)
                    n += 1 
                    
            if (lett == '$') and (n % 2 != 0):
                    lines[line] = lines[line].replace("$","\\)",1)
                    n += 1
                    

#----------------------------------------------

# 2. filling the fields of the Data:

#----------------------------------------------

    #filling Data with titles:
def fill_with_titles(lines):
    for line in range(0,len(lines)):
        if ("." in lines[line]) and (":" in lines[line][-2::]) and ("\\" not in lines[line][-2::]):
            Data[1].append(lines[line])

#----------------------------------------------

    # filling Data with tags:
def fill_with_tags(lines):
    tag = "none"
    for line in range(0,len(lines)):
        if ("##" in lines[line]):
            tag = lines[line][2::]
        if ("." in lines[line]) and (":" in lines[line][-2::]) and ("\\" not in lines[line][-2::]):
            Data[0].append(tag)
            
#----------------------------------------------

    #filling Data with content:
def fill_with_content(lines):
    
    content = ""
    end_tex = []
    beg_tex = []
    ranges = []
    
    # filling the indicies:
    
    for line in range(0,len(lines)):
        if ("." in lines[line]) and (":" in lines[line][-2::]) and ("\\" not in lines[line][-2::]):
            beg_tex.append(line)
            if len(beg_tex) > 1:
                end_tex.append(line - 1)
    end_tex.append(len(lines)-1) # to have a consistant numbering to increase later in the fillings (the end_tex respond to one less, so should the last element)
    
    # getting ranges:
    
        #appending last latex entry into the beginning tex list so that 
        #the last elements can be written easily:
        # using "blocks" as indicators for the loop to divide up the work
        #by going through all lines between the beginning of the block and
        #less than or equal the end of the next block, this is why we added the 
        #last element above to the beg_tex list, namely, to add the last element of 
        # the last block
    
    for block in range( 0, len(beg_tex) ):
        # Because both end_tex and beg_tex hav the same length, we can just enumerate the ranges
        # with simple loop:
        # storing the results
        ranges.append(beg_tex[block])
        ranges.append(end_tex[block])

    # getting the content inside Data:
    
    for cont in range(0,len(ranges)):
        content = ""
        if cont%2 == 0: #this ensures that we start with beggining blocks, due to the structure of the ranges
            for line in range(ranges[cont]+1,ranges[cont+1]+1):
                if "##" not in lines[line]: # to make sure the chapters are not included in the contents
                    content += lines[line]
            Data[2].append(str(content))

#----------------------------------------------
    # Program:

replace_double_money(lines)
replace_single_money(lines)
fill_with_titles(lines)
fill_with_tags(lines)
fill_with_content(lines)

    # Saving the Data as .csv

File = pd.DataFrame(Data) 
File = File.T
Text = input("Enter Deck Name:")
new_header = File.iloc[0] 
File = File[1:] 
File.columns = new_header 
File.to_csv("Anki" + Text + ".csv", index = False)
#----------------------------------------------