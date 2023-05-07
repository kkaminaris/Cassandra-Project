import csv
import re

firstrow = True

#leave blank lines in new movie.csv so we can random access any movie by its id
with open('movie.csv','r') as infile, open('movie1.csv','w') as outfile:
    csvr = csv.reader(infile, delimiter=',')
    csvw = csv.writer(outfile, delimiter=',')
    emptyRowCounter = 0
    blankLines = 0
    for row in csvr:
        #header treatment
        if firstrow:
            firstrow = False
            temprow = row
            csvw.writerow(temprow)
        else:
            temprow = row
            temp = csvr.line_num
            blankLines = 0
            while (temp + emptyRowCounter) != (int(temprow[0])+1):
                csvw.writerow([])
                blankLines = blankLines + 1
                temp = temp + 1
            emptyRowCounter = emptyRowCounter + blankLines
            csvw.writerow(temprow)

firstrow = True

#clear data formatting
with open('movie1.csv','r') as infile, open('movie2.csv','w') as outfile:
    csvr = csv.reader(infile, delimiter=',')
    csvw = csv.writer(outfile, delimiter=',')
    for row in csvr:
        #edit header
        if firstrow:
            firstrow = False
            temprow = row
            temprow.append("year")
            csvw.writerow(temprow)
        else:
            if row != []:
                temprow = row
                #get rid of unwanted characters
                temprow[1] = temprow[1].replace(" ", " ")
                temprow[1] = temprow[1].replace("–", "")
                temprow[1] = temprow[1].replace("(", "")
                temprow[1] = temprow[1].replace(")", "")
                temprow[1] = temprow[1].replace("\"", "")
                temprow[1] = temprow[1].replace("\'", "")
                name = temprow[1]
                #check for character '-' in year
                if name[-1] == '-':
                    name = name[:-1]
                    temprow[1] = name
                #check for no space between last word and year
                pattern = re.compile(".*[a-zA-Z]+[0-9][0-9][0-9][0-9]$")
                if pattern.match(name):
                    p = re.compile("[a-zA-Z]+[0-9][0-9][0-9][0-9]$")
                    for m in p.finditer(name):
                        name = name[:len(name)-4] + ' ' + name[len(name)-4:]
                        temprow[1] = name
                #split title and year
                list = temprow[1].split(" ")
                #get rid of empty last element
                if list[len(list)-1] == '':
                    list.pop()
                #check for character '-' in year again
                if list[len(list)-1].find('-') != -1:
                    list[len(list)-1] = list[len(list)-1][:-5]
                #check for missing year data
                pattern = re.compile("([0-9][0-9][0-9][0-9])")
                if pattern.match(list[len(list)-1]):
                    temprow.append(list[len(list)-1])
                    list.pop()
                else:
                    temprow.append("null")
                #rewrite title
                title = ""
                for word in list:
                    title = title + word + " "
                title = title[:-1]
                temprow[1] = title

                #rewrite the genres column as a set
                list = temprow[2].split("|")
                temp = "{"
                for element in list:
                    temp = temp + '\'' + element + '\'' + ','
                temp = temp[:-1]
                temp = temp + '}'
                temprow[2] = temp

                csvw.writerow(temprow)
            else:
                csvw.writerow([])