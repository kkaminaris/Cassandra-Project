import csv
import datetime

firstrow = True

#save movie.csv in a list for random access
with open('movie2.csv', 'r') as infile:
    csvr = csv.reader(infile, delimiter=',')
    movies = list(csvr)

with open('rating.csv','r') as infile, open('movies_by_rating1.csv','w') as outfile:
    csvr = csv.reader(infile, delimiter=',')
    csvw = csv.writer(outfile, delimiter=',')
    #read through files
    for row in csvr:
        #edit header
        if firstrow:
            firstrow = False
            temprow = row
            temprow.append("rating_month")
            temprow.append("rating_year")
            temprow.append("movie_title")
            temprow.append("movie_year")
            csvw.writerow(temprow)
        else:
            temprow = row

            #keep year from datetime
            year = datetime.datetime.strptime(temprow[3],'%Y-%m-%d %H:%M:%S').strftime('%Y')

            #keep month from datetime
            month = datetime.datetime.strptime(temprow[3],'%Y-%m-%d %H:%M:%S').strftime('%m')
            
            temprow.append(month)
            temprow.append(year)
            temprow.append(movies[int(temprow[1])][1])
            temprow.append(movies[int(temprow[1])][3])
            csvw.writerow(temprow)