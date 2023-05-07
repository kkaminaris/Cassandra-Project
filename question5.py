import csv
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
    rows = session.execute('SELECT * from movies_by_tag where tag_name = \'comedy\' order by avg_rating desc limit 20')
    for row in rows:
        temprow = []
        temprow.append(row.movie_id)
        temprow.append(row.movie_title)
        temprow.append(row.movie_year)
        temprow.append(round(row.avg_rating, 1))
        temprow.append(row.tag_name)
        csvw.writerow(temprow)