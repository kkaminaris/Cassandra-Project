import csv

firstrow = True

tagDict = {}

#save movie.csv in a list for random access
with open('movie5.csv', 'r') as infile:
    csvr = csv.reader(infile, delimiter=',')
    movies = list(csvr)

#make dictionary
with open('tag.csv', 'r') as infile:
    csvr = csv.reader(infile, delimiter=',')
    for row in csvr:
        #ignore header
        if firstrow:
            firstrow = False
        else:
            temprow = row
            #fill dictionary
            try:
                tagDict[temprow[2]].add(temprow[1])
            except KeyError:
                tagDict[temprow[2]] = {temprow[1]}

#for x, y in tagDict.items():
#    print(x, y)

firstrow = True

#make outfile
with open('movies_by_tag.csv','w') as outfile:
    csvw = csv.writer(outfile, delimiter=',')
    #make header
    temprow = []
    temprow.append("tag")
    temprow.append("movieID")
    temprow.append("movieTitle")
    temprow.append("movieYear")
    temprow.append("avgRating")
    csvw.writerow(temprow)
    #write rest of lines
    temprow = []
    for tag, set in tagDict.items():
        for id in set:
            temprow.append(tag)
            temprow.append(id)
            temprow.append(movies[int(id)][1])
            temprow.append(movies[int(id)][3])
            temprow.append(movies[int(id)][4])

            csvw.writerow(temprow)
            temprow.clear()