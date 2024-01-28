# Cassandra-Project

Simple Casssandra-based DB to organize and manage Netflix-like application data.

Data sets can be found [here](https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset).

All use-cases were analysed, and tranformed into their respective table. `import[1-5].py` and `movie_remap.py` are used to manipulate the csv files. Then `dsbulk` was used to load the DB. Finally with `question[1-5].py` we connect to `AstraDB` and return the data that we want.

#### `Technologies used:`

- Python
- AstraDB
- dsbulk

#### `Use-cases developed:`

- Q1. Show the 30 higher rated movies from 01/01/2015 to 15/01/2015
- Q2. Show movie details for Jumanji (category, avg rating, top-5 tags)
- Q3. Show movies under the category "adventure" sorted by production year
- Q4. Show movies with "star" in their title
- Q5. Show the 20 higher rated movies that have the tag "comedy"

#### `Chebotko diagram:`

<p align="center">
<img align="center" alt="chebotko" width="50%" src="./chebotko.png?raw=true" />
</p>

#### `Original documents in greek:`
In `project_big_data_2021-22.pdf` you can find the project description as given by my professor in `University of Patras`.

In `Αναφορά Συστήματα Διαχείρισης Δεδομένων Μεγάλου Όγκου.docx.pdf` you can find my respective report.

