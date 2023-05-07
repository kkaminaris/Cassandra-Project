import csv ,operator
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

#connect to astra db
cloud_config= {
        'secure_connect_bundle': 'secure-connect-cassandra-project.zip'
}
auth_provider = PlainTextAuthProvider('FnulehdTssEyNqEaXQehBZtF', '7-ZwXnfOsLzG8aRmYORZzC+u.Bw1HGRvFhtkvN,LZ6HG13z.sJOFCY3H2uYsQfzDYfhqPQkeFwHjLz_IKtj6ipHOZywaZPBcW1lAuuLJ_5W4WXdmbz1vG93Kh4Y4Qj+-')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect("moviesproject")

#run querry
with open('test.csv','w') as outfile:
    csvw = csv.writer(outfile, delimiter=',')
    rows = session.execute('SELECT * from movies_by_rating where rating_year = 2015 and rating_month = 1 and rating_date >= \'2015-01-01 00:00:00+0000\' and rating_date < \'2015-01-16 00:00:00+0000\'')
    for row in rows:
        temprow = []
        temprow.append(row.rating_year)
        temprow.append(row.rating_month)
        temprow.append(row.rating_date)
        temprow.append(row.movie_id)
        temprow.append(row.movie_title)
        temprow.append(row.movie_year)
        temprow.append(row.rating_value)
        csvw.writerow(temprow)

firstrow = True

#make lists
ratingSum = []
ratingCount = []
movieTitle = []
movieYear = []

#init lists
for x in range(132000):
    ratingCount.insert(x, 0)
    ratingSum.insert(x, 0)
    movieTitle.insert(x, 'null')
    movieYear.insert(x, 0)

#fill lists
with open('test.csv', 'r') as infile:
    csvr = csv.reader(infile, delimiter=',')
    for row in csvr:
        if firstrow:
            firstrow = False
        else:
            temprow = row
            if movieTitle[int(temprow[3])] == 'null':
                movieTitle[int(temprow[3])] = temprow[4]
            if movieYear[int(temprow[3])] == 0:
                movieYear[int(temprow[3])] = temprow[5]
            if ratingCount[int(temprow[3])] == 0:
                ratingSum[int(temprow[3])] = float(temprow[6])
                ratingCount[int(temprow[3])] = 1
            else:
                ratingCount[int(temprow[3])] = ratingCount[int(temprow[3])] + 1
                ratingSum[int(temprow[3])] = ratingSum[int(temprow[3])] + float(temprow[6])
            #print("count = ", ratingCount[int(temprow[3])])
            #print("sum = ", ratingSum[int(temprow[3])])

#mid-point output
with open('answer1.csv','w') as outfile:
    csvw = csv.writer(outfile, delimiter=',')
    temprow = []
    temprow.append("movie_title")
    temprow.append("movie_year")
    temprow.append("avgRating")
    csvw.writerow(temprow)
    for movie_id in range(132000):
        if movieTitle[movie_id] == 'null':
            continue

        temprow = []

        #calculate avg_rating
        average = ratingSum[movie_id] / ratingCount[movie_id]
        temprow.append(movieTitle[movie_id])
        temprow.append(movieYear[movie_id])
        temprow.append(round(average, 1))
        csvw.writerow(temprow)

#sort data
data = csv.reader(open('answer1.csv'),delimiter=',')

data = sorted(data, key=operator.itemgetter(2), reverse=True) 

counter = 0

#make outfile
with open('answer1sorted.csv','w') as outfile:
    csvw = csv.writer(outfile, delimiter=',')
    for row in data:
        if counter > 30:
            break
        csvw.writerow(row)
        counter = counter + 1