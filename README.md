# Cassandra-Project

A simple Cassandra-based database designed for organizing and managing data in a Netflix-like application. The project involves analyzing various use-cases, transforming them into their respective tables, and utilizing the Python scripts `import[1-5].py` and `movie_remap.py` for data manipulation. The data is then loaded into AstraDB using `dsbulk`, and querying is performed using `question[1-5].py` scripts.

Data sets can be found [here](https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset).

## Technologies Used

- Python
- AstraDB
- dsbulk

## Developed Use-Cases

1. **Q1:** Show the 30 highest-rated movies from 01/01/2015 to 15/01/2015.
2. **Q2:** Display movie details for Jumanji (category, average rating, top-5 tags).
3. **Q3:** Show movies under the category "adventure," sorted by production year.
4. **Q4:** Show movies with "star" in their title.
5. **Q5:** Show the 20 highest-rated movies with the tag "comedy."

## Chebotko Diagram

<p align="center">
<img align="center" alt="chebotko" width="70%" src="./chebotko.png?raw=true" />
</p>

## Documentation in Greek

- **Project Description:** Find the original project description in [`project_big_data_2021-22.pdf`](project_big_data_2021-22.pdf) provided by the professor at the University of Patras.
- **Report:** Access my detailed report in [`Αναφορά_Συστήματα_Διαχείρισης_Δεδομένων_Μεγάλου_Όγκου.docx.pdf`](Αναφορά_Συστήματα_Διαχείρισης_Δεδομένων_Μεγάλου_Όγκου.docx.pdf).
