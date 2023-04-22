# Twitter-Scraping
## Python scripting, Data Collection, MongoDB, Streamlit

![MADE WITH PYTHON](http://ForTheBadge.com/images/badges/made-with-python.svg)  [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://)

Disclaimer: This project is built for research purposes only. I, ***Gladin K. Varghese*** , as the developer am not responsible for any misuse of this project. I believe that this kind of technology should be accessible if needed for the correct reasons.
  
 ### This project is built using these libraries and modules:
 * Streamlit - Streamlit is an open-source app framework for Machine Learning and Data Science teams.
 * Pandas - Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.
 * Pymongo - PyMongo is a Python distribution containing tools for working with MongoDB, and is the recommended way to work with MongoDB from Python.
 * Snscrape - Snscrape is a scraper for social networking services (SNS). It scrapes things like user profiles, hashtags, or searches and returns the discovered items
 * Datetime - The datetime module supplies classes for manipulating dates and times.

## Hosted on Streamlit Cloud [(read more about Streamlit Cloud)](https://streamlit.io/cloud):
[Twitter Scraping](https://)

## Article on Medium

## ![Demo Video](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)

## Workflow
step-by-step explanation of the workflow of the Twitter Scraping App:

1. The user opens the app in a web browser.
2. The app loads the required libraries, including snscrape, pandas, pymongo, streamlit, datetime, json, and PIL.
3. The app defines a function called "Scrapingdata" that scrapes Twitter for tweets based on user input. The function takes in four parameters: a hashtag, start and end date, and the number of tweets to scrape.
4. The app sets up the page configuration using the st.set_page_config() function, including the title, icon, layout, and sidebar state.
5. The app creates a menu section using the st.sidebar.selectbox() function, allowing the user to choose one of the available options: Home, About, Search, Display, and Download.
6. If the user selects "Home" from the menu, the app displays a landing page with the app title, description, and an image of Elon Musk using the st.title(), st.markdown(), and st.image() functions.
7. If the user selects "About" from the menu, the app displays information about various technologies and frameworks used in the app using the st.expander() function.
8. If the user selects "Search" from the menu, the app prompts the user to input a hashtag, start and end date, and the number of tweets to scrape using the st.text_input(), st.date_input(), and st.number_input() functions.
9. When the user clicks the "Scrape" button, the app calls the "Scrapingdata" function to scrape the requested tweets from Twitter using snscrape and stores the results in a pandas DataFrame.
10. The app displays the scraped tweets data in a table using the st.dataframe() function.
11. If the user selects "Display" from the menu, the app displays the scraped tweets data in a visual format using various charts and graphs created using the matplotlib library and the st.pyplot() function.
12. If the user selects "Download" from the menu, the app allows the user to download the scraped tweets data as a CSV or JSON file using the pandas.DataFrame.to_csv() and pandas.DataFrame.to_json() functions and the st.download_button() function.

Overall, the workflow of the Twitter Scraping App involves taking user input, scraping tweets data from Twitter, storing and displaying the scraped data in various formats, and allowing the user to download the data for further analysis.

To execute this script, navigate to the Terminal and enter the command below. This will open a new window in your browser where you can interact with the Streamlit user interface:

    streamlit run twitterscraper.py

