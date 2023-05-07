import csv

firstrow = True

#file setup
with open('movie5.csv','r') as infile, open('movies_by_genres.csv','w') as outfile:
    csvr = csv.reader(infile, delimiter=',')
    csvw = csv.writer(outfile, delimiter=',')
    for row in csvr:
        #header treatment
        if firstrow:
            firstrow = False
            temprow = row
            temprow.append("movie_genre")
            csvw.writerow(temprow)
        else:
            if row != []:
                temprow = row
                #make set
                genres = temprow[2].split(",")
                for genre in genres:
                    genre = genre.replace("{", "")
                    genre = genre.replace("}", "")
                    genre = genre.replace("\'", "")
                    temprow.append(genre)
                    csvw.writerow(temprow)
                    temprow.remove(temprow[5])
            else:
                csvw.writerow([])