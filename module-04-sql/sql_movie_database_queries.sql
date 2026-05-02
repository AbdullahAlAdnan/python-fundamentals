-- Module 4 Assignment — SQL Queries
-- Course: Data Science Program
-- Database: Movie Rental Company

-- Table Creation
CREATE TABLE Movies(
    MovieID INT PRIMARY KEY,
    Title VARCHAR(50),
    Genre VARCHAR(50),
    ReleaseYear INT,
    Rating FLOAT,
    BoxOfficeRevenue BIGINT,
    Director VARCHAR(50)
);

-- Sample Data
INSERT INTO Movies (MovieID, Title, Genre, ReleaseYear, Rating, BoxOfficeRevenue, Director) VALUES
(1, 'Inception', 'Sci-Fi', 2010, 8.8, 830000000, 'Christopher Nolan'),
(2, 'Titanic', 'Romance', 1997, 7.8, 2200000000, 'James Cameron'),
(3, 'The Godfather', 'Crime', 1972, 9.2, 134000000, 'Francis Ford Coppola'),
(4, 'Avatar', 'Sci-Fi', 2009, 7.9, 2840000000, 'James Cameron'),
(5, 'Interstellar', 'Sci-Fi', 2014, 8.6, 677000000, 'Christopher Nolan'),
(6, 'Parasite', 'Thriller', 2019, 8.6, 264000000, 'Bong Joon Ho'),
(7, 'The Dark Knight', 'Action', 2008, 9.0, 1000000000, 'Christopher Nolan'),
(8, 'Schindlers List', 'Drama', 1993, 9.0, 322000000, 'Steven Spielberg'),
(9, 'The Shawshank Redemption', 'Drama', 1994, 9.3, 28300000, 'Frank Darabont'),
(10, 'Pulp Fiction', 'Crime', 1994, 8.9, 213000000, 'Quentin Tarantino');

-- Q1: Retrieve all information about movies directed by Christopher Nolan
SELECT * FROM Movies
WHERE Director = 'Christopher Nolan';

-- Q2: Find all distinct genres in the Movies table
SELECT DISTINCT Genre FROM Movies;

-- Q3: Display the top 5 highest-rated movies sorted by rating descending
SELECT * FROM Movies
ORDER BY Rating DESC
LIMIT 5;

-- Q4: List all movies released before the year 2000
SELECT * FROM Movies
WHERE ReleaseYear < 2000;

-- Q5: Show the total number of movies in each genre
SELECT Genre, COUNT(*) AS TotalMovies
FROM Movies
GROUP BY Genre;

-- Q6: Find the total revenue of all movies in the Sci-Fi genre
SELECT SUM(BoxOfficeRevenue) AS TotalRevenue
FROM Movies
WHERE Genre = 'Sci-Fi';

-- Q7: Retrieve titles of movies with rating greater than 8.5 but less than 9.0
SELECT Title FROM Movies
WHERE Rating > 8.5 AND Rating < 9.0;

-- Q8: Display movies that have the word 'The' in their title
SELECT Title FROM Movies
WHERE Title LIKE '%The%';

-- Q9: Find the movie with the highest box office revenue
SELECT Title, BoxOfficeRevenue FROM Movies
ORDER BY BoxOfficeRevenue DESC
LIMIT 1;

-- Q10: Retrieve the average rating of all movies released after the year 2000
SELECT ROUND(AVG(Rating), 2) AS AverageRating FROM Movies
WHERE ReleaseYear > 2000;
