# scrapy_project
## Scrapping in Python by using Scrapy

## Objective of Project
- In this project, we are doing scrapping while using Scrapy library of python. We have get validated data from           https://www.goodreads.com/book/popular_by_date


## Setup Project

1. Clone the project using following command
```
git clone https://github.com/AMOIZ0866/scrapy_project.git
```

2. Make sure you have python 3 installed in your system

3. Make sure you have install these packages of python 
    -  pip3 install scrapy  
    -  pip3 install selenium 
    -  brew cask install chromedriver
          
    
## Procedure
   - In Spider Folder in the directory we have file name with "scrapping.py" with name="blogspider" to run this file.(This file contains all the code related to scrapping)
   
   - Than we have main.py where we have function of class Analysis to analyze the data:
   - "analysis.get_high_rating()" for making a small graph showing the top 10 highest rated books.
   - "analysis.get_author_with_most_books()" for list of authors who had the most number of books in the popular book
   - "analysis.get_genres_with_number_of_books()" for list all the genres in order of number of books.
   - "analysis.get_avg_rating_genres()" for calculating the average rating of books in a genre.

## Git Branching Structure
- Default latest branch is **Staging**
- Dev is child branch for development
- Every task branch finally merged in Staging upon completion/review.

## How to deploy new changes
- Create a new branch from **staging** branch
- Update the codebase according to the change-set required
- Create a **Pull Request** with **staging** branch
- Review & Merge that PR

