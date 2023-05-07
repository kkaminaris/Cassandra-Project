import csv

firstrow = True

moviesDict = {}

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
                moviesDict[temprow[1]].update({temprow[2]: moviesDict[temprow[1]][temprow[2]]+1})
            except KeyError:
                try:
                    moviesDict[temprow[1]].update({temprow[2]: 1})
                except KeyError:
                    moviesDict[temprow[1]] = ({temprow[2]: 1})

#for x, y in moviesDict.items():
#    print(x, y)

#sort dictionaries in moviesDict
#for movieID, tagDict in moviesDict.items():
#    tagList = sorted(tagDict.items(), key=lambda x:x[1], reverse=True)
#    moviesDict[movieID] = dict(tagList)

firstrow = True

#make outfile
with open('movie5.csv', 'r') as infile, open('movie_details.csv','w') as outfile:
    csvr = csv.reader(infile, delimiter=',')
    csvw = csv.writer(outfile, delimiter=',')
    for row in csvr:
        #make header
        if firstrow:
            firstrow = False
            temprow = row
            temprow.append("tag")
            temprow.append("tagCounter")
            csvw.writerow(temprow)
        else:
            temprow = row
            if temprow == []:
                continue
            try:
                for x, y in moviesDict[temprow[0]].items():
                    temprow.append(x)
                    temprow.append(y)
                    csvw.writerow(temprow)
                    temprow = temprow[:-2]
            except KeyError:
                temprow.append('NULL')
                temprow.append('0')
                csvw.writerow(temprow)

            

