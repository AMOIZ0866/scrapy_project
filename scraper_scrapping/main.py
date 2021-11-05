from scraper_scrapping.Analyst import Analysis as ans
if __name__ == '__main__':
    # Analysis of data#
    analysis = ans()
    analysis.get_high_rating()
    # analysis.get_author_with_most_books()
    # analysis.get_genres_with_number_of_books()
    # analysis.get_avg_rating_genres()