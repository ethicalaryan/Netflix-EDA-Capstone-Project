#!/usr/bin/env python
# coding: utf-8

# ## Netflix Data Analysis Project
# 
# THE NETFLIX EDA PROJECT REVOLVES AROUND
# EXPLORING AND ANALYZING A DATASET RELATED TO
# NETFLIX CONTENT. THE DATASET LIKELY INCLUDES
# INFORMATION ABOUT MOVIES AND TV SHOWS
# AVAILABLE ON THE PLATFORM. THE PURPOSE OF THE
# PROJECT IS TO PERFORM EXPLORATORY DATA
# ANALYSIS TO EXTRACT MEANINGFUL INSIGHTS AND
# DRAW CONCLUSIONS FROM THE DATA.

# . Project Introduction
# 
# . Dataset Overview
# 
# . Data Cleaning
# 
# . Exploratory Analysis
# 
# . Visualizations
# 
# . Key Insights
# 
# . Conclusion

# ## Import Libraries

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(style='whitegrid')


# ## Load Dataset

# In[5]:


df = pd.read_csv("netflix_titles.csv")
df.head()


# ## Dataset Overview

# In[6]:


df.shape
df.info()
df.columns
df.describe(include='object')


# ## Missing Values Check

# In[7]:


msno.matrix(df)
plt.show()

df.isnull().sum()


# ## Data Cleaning

# In[13]:


df.drop_duplicates(inplace=True)
df.dropna(subset=['type', 'title'], inplace=True)
df['director'].fillna('Unknown', inplace=True)
df['country'].fillna('Unknown', inplace=True)
df['date_added'].fillna('Not Provided', inplace=True)
df['rating'].fillna(df['rating'].mode()[0], inplace=True)


# ## Movies vs TV Shows

# In[14]:


sns.countplot(data=df, x='type', palette='Set2')
plt.title('Movies vs TV Shows on Netflix')
plt.show()


# ## Descriptive Statistics

# In[15]:


df['duration'].value_counts().head()


# ## Genre Distribution

# In[16]:


genres = df['listed_in'].str.split(', ', expand=True).stack()
top_genres = genres.value_counts().head(10)

sns.barplot(x=top_genres.values, y=top_genres.index, palette='Blues_r')
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Number of Titles")
plt.show()


# ## Release Years Distribution

# In[17]:


df['release_year'].value_counts().head(10).plot(kind='bar', color='orange')
plt.title("Content Released by Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.show()


# ## Country-Wise Content

# In[19]:


top_countries = df['country'].value_counts().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index, palette='Set3')
plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Number of Titles")
plt.show()


# ## Top 10 Countries by Content

# In[20]:


top_countries = df['country'].value_counts().head(10)
top_countries.plot(kind='bar', color='tomato')
plt.title('Top 10 Countries with Most Content')
plt.xlabel('Country')
plt.ylabel('Number of Titles')
plt.xticks(rotation=45)
plt.show()


# ## Year-wise Content Addition

# In[11]:


df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year

sns.histplot(df['year_added'].dropna(), bins=20, color='purple')
plt.title('Content Addition Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.show()


# ## Most Common Genres

# In[12]:


genres = df['listed_in'].str.split(', ', expand=True).stack()
top_genres = genres.value_counts().head(10)

top_genres.plot(kind='barh', color='skyblue')
plt.title('Top 10 Most Common Genres')
plt.xlabel('Number of Titles')
plt.gca().invert_yaxis()
plt.show()


# ## Time Series – Year of Addition

# In[21]:


df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year

sns.histplot(df['year_added'].dropna(), kde=False, bins=20, color='purple')
plt.title("Content Added Over the Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.show()


# ## Content Ratings

# In[22]:


sns.countplot(y='rating', data=df, order=df['rating'].value_counts().index, palette='cool')
plt.title("Distribution of Content Ratings")
plt.show()


# ## Movie Duration Analysis

# In[23]:


movie_df = df[df['type'] == 'Movie']
movie_df['duration_minutes'] = movie_df['duration'].str.extract('(\d+)').astype(float)

sns.histplot(movie_df['duration_minutes'], bins=30, color='green')
plt.title("Movie Duration Distribution")
plt.xlabel("Duration (minutes)")
plt.show()


# ## Unique Genre Count

# In[24]:


unique_genres = genres.nunique()
print("Total Unique Genres:", unique_genres)


# ## Genre Trends Over Time

# In[25]:


genre_year = df.dropna(subset=['date_added'])
genre_year['year'] = genre_year['date_added'].dt.year

genre_df = genre_year['listed_in'].str.split(', ', expand=True).stack().reset_index(level=1, drop=True).to_frame('Genre')
genre_df['year'] = genre_year['year']

trend = genre_df.groupby(['year', 'Genre']).size().unstack().fillna(0)
trend[['Dramas', 'Comedies', 'Documentaries']].plot(figsize=(12,6))
plt.title("Genre Trends Over Time")
plt.ylabel("Count")
plt.show()


# ## Conclusion

# - Based on our analysis:
# 
# - Netflix has a large number of movies.
# 
# - Most content comes from USA and India.
# - Netflix has more Movies than TV Shows.
# 
# - Top Content Countries: United States, India, UK.
# 
# - Most content added between 2017-2020.
# 
# - Top Genres: Dramas, Documentaries, Comedies.
# 
# - Ratings are most common with TV-MA, TV-14.
# 
# - Duration distribution is mostly between 90-120 minutes.
# 
# - Genre trends show Dramas and Comedies to be consistently popular.
# - Content on Netflix has grown rapidly since 2016.
# 
# - Dramas and documentaries are very popular.
# 
# 📌 Recommendations:
# 
# - Adding more content from countries like India.
# 
# - Improving recommendations based on users' language preferences.
# 
# 

# In[ ]:




