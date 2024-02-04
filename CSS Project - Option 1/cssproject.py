# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 22:21:47 2024

@author: Neno
"""

import pandas as pd

# Load the dataset
file_path = 'C:/Users/Neno/Downloads/movie_dataset.csv'
df = pd.read_csv(file_path)
print(df.info())

# Rename columns to remove spaces
df.columns = df.columns.str.replace(' ', '')

# Handle missing values
# Fill missing values with the mean 
df['Revenue(Millions)'].fillna(df['Revenue(Millions)'].mean(), inplace=True)
# Fill missing values with the mode
df['Metascore'].fillna(df['Metascore'].mode()[0], inplace=True)

#1. Highest rated movie in the dataset
highest_rated_movie_index = df['Rating'].idxmax()
highest_rated_movie = df.loc[highest_rated_movie_index]
print("Highest Rated Movie:")
print(highest_rated_movie['Title'])

#2. average revenue of all movies in the dataset
average_revenue = df['Revenue(Millions)'].mean()
print("Average Revenue of All Movies:", average_revenue)

#3. average revenue of movies from 2015 to 2017 in the dataset
filtered_movies = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
average_revenue_2015_to_2017 = filtered_movies['Revenue(Millions)'].mean()
print("Average Revenue of Movies from 2015 to 2017:", average_revenue_2015_to_2017)

#4. Movies released in the year 2016
movies_2016 = df[df['Year'] == 2016]
num_movies_2016 = len(movies_2016)
print("Number of Movies Released in 2016:", num_movies_2016)

#5. movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']
num_nolan_movies = len(nolan_movies)
print("Number of Movies Directed by Christopher Nolan:", num_nolan_movies)

#6. movies in the dataset have a rating of at least 8.0
high_rated_movies = df[df['Rating'] >= 8.0]
number_of_high_rated_movies = len(high_rated_movies)
print(f'The number of movies with a rating of at least 8.0 is: {number_of_high_rated_movies}')

#7. median rating of movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']
median_rating_nolan_movies = nolan_movies['Rating'].median()
print(f'The median rating of movies directed by Christopher Nolan is: {median_rating_nolan_movies}')

#8. year with the highest average rating
average_rating_by_year = df.groupby('Year')['Rating'].mean()
year_highest_avg_rating = average_rating_by_year.idxmax()
highest_avg_rating = average_rating_by_year.max()
print(f"The year with the highest average rating is {year_highest_avg_rating} with an average rating of {highest_avg_rating:.2f}")

###9. percentage increase in number of movies made between 2006 and 2016
movies_by_year = df['Year'].value_counts()
# Extract counts for 2006 and 2016
count_2006 = movies_by_year.get(2006, 0)
count_2016 = movies_by_year.get(2016, 0)
# Calculate the percentage increase
percentage_increase = ((count_2016 - count_2006) / count_2006) * 100
print(f"The percentage increase in the number of movies between 2006 and 2016 is: {percentage_increase:.2f}%")

###10. most common actor in all the movies
# Split the multiple actors in the 'Actors' column into individual rows
df_actors = df['Actors'].str.split(', ', expand=True).stack().reset_index(level=1, drop=True).rename('Actor')
# Find the most common actor
most_common_actor = df_actors.value_counts().idxmax()
print(f"The most common actor in all the movies is: {most_common_actor}")

###11. unique genres in the dataset
all_genres = df['Genre'].str.split(',').explode()
# Get the count of unique genres
num_unique_genres = all_genres.nunique()
print(f"The number of unique genres in the dataset is: {num_unique_genres}")

###12. correlation of the numerical features
# Exclude non-numeric columns
numeric_df = df.select_dtypes(include=['float64', 'int64'])
# Calculate the correlation matrix for numerical features
correlation_matrix = numeric_df.corr()
print("Correlation Matrix:")
print(correlation_matrix)