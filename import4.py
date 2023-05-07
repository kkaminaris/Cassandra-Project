import csv

firstrow = True

#file setup
with open('movie5.csv','r') as infile, open('movies_by_keywords.csv','w') as outfile:
    csvr = csv.reader(infile, delimiter=',')
    csvw = csv.writer(outfile, delimiter=',')
    for row in csvr:
        #edit header
        if firstrow:
            firstrow = False
            temprow = row
            temprow.remove(temprow[4])
            temprow.remove(temprow[2])
            temprow.append("movie_title_word")
            csvw.writerow(temprow)
        else:
            if row != []:
                temprow = row

                #remove rating
                temprow.remove(temprow[4])

                #remove genres
                temprow.remove(temprow[2])

                #remove commas, ':' and " from title
                title = temprow[1]
                title = title.replace("\"", "")
                title = title.replace(",", "")
                title = title.replace(":", "")


                #prepare list
                list = title.split()

                for element in list:
                    temprow.append(element)
                    csvw.writerow(temprow)
                    temprow.remove(temprow[3])
            else:
                csvw.writerow([])