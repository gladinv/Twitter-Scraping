
# Import relevant libraries
import snscrape.modules.twitter as sntwitter
import pandas as pd
import pymongo
import streamlit as st
from datetime import date
import json
from PIL import Image

# List of scraped tweets based on the user input
def Scrapingdata(Hashtag,start_date,End_date,tweets_count):
      tweets_list=[]
      for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{Hashtag} since:{start_date} until:{End_date}', top = True).get_items()):
           if i>=tweets_count:
               break
           tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.url, tweet.retweetCount, tweet.source, tweet.likeCount,tweet.replyCount,tweet.lang])
      return(tweets_list)

# Menu section of the appy
st.set_page_config(page_title="Twitter Scraping", page_icon=':bird:', layout="centered", initial_sidebar_state="expanded")
menu=["Home","About","Search","Display","Download"]
choice=st.sidebar.selectbox("menu",menu)

# Home page of the app
if choice=="Home": 
    st.title(':black[_Twitter Scraping App_]')
    st.markdown("_***This app was created with the Streamlit app framework. The app scrapes Twitter data based on user-inputted hashtags/keywords and date range. Additionally, it allows users to upload tweets data to MongoDB and download it as a CSV or JSON file.***_")
    img=Image.open("elonmusk.webp")
    st.image(img)

# About page of the app
elif choice=="About":
    with st.expander("**Twitter Scraping**"):
        st.write("Twitter Scraper will scrap data from public twitter profiles. It can collect data such as **date, id, url, tweet content, reply count, retweet, count, language, like count, followers etc** from tweets")
    with st.expander("**Snscrape**"):
        st.write("Snscrape is a scraper for social networking services (SNS). It scrapes things like user profiles, hashtags, or searches and returns the discovered items, e.g. the relevant posts.")
    with st.expander("**Mongodb**"):
        st.write("MongoDB is an open-source document-oriented database that is designed to store a large scale of data and also allows you to work with that data very efficiently.")
    with st.expander("**Streamlit**"):
        st.write("Streamlit is an open source app framework in python language. It helps us create beautiful web-apps for data science and machine learning in a little time. It is compatible with major python libraries such as scikit-learn, keras, pytorch, latex, numpy, pandas, matplotlib, etc.")
        st.balloons()

# Search and Scrape tweets
elif choice=="Search":
    Hashtag=st.text_input("Enter Hashtag or Keyword")
    start_date=st.date_input("Enter starting date:(YYYY-MM-DD)")
    End_date=st.date_input("Enter end date:(YYYY-MM-DD)")
    tweets_count=st.number_input("Enter Tweet count",min_value=1,max_value=1500,step=2)
    if Hashtag:
        submit=st.checkbox("**Scrape Tweets**")
        if submit:

             data=Scrapingdata(Hashtag,start_date,End_date,tweets_count)
             st.success("Data scraped successfully!")
             st.balloons()
             def data_frame(data):
                    return pd.DataFrame(data,columns=['Datetime', 'Tweet Id', 'Text', 'Username',"url","retweetCount","source","like_count","replycount","lan"])
             df=data_frame(data)
            
# Connect to MongoDB database
             client = pymongo.MongoClient("mongodb://localhost:27017")
             db = client.Twitter
             records=db.scrapping
             today=str(date.today())
             scr_data={"Scraped_word":Hashtag,"Scraped_date":today,"Scraped_data":df.to_dict("list")}
             records.delete_many({})
             records.insert_one(scr_data)
             st.success("Uploaded to MongoDB successfully!")
             st.balloons()

    else:
         st.checkbox("Scrape Tweet Data",disabled=True)

# Display scraped data
elif choice=="Display":
    Hashtag=st.sidebar.text_input("Enter Hashtag or Keyword")
    start_date=st.sidebar.date_input("Enter starting date:(YYYY-MM-DD)")
    End_date=st.sidebar.date_input("Enter end date:(YYYY-MM-DD)")
    tweets_count=st.sidebar.number_input("Enter Tweet count",min_value=1,max_value=1500,step=2)
    list_tweet=Scrapingdata(Hashtag,start_date,End_date,tweets_count)
    def data_frame(data):
         return(pd.DataFrame(data,columns=['Datetime', 'Tweet Id', 'Text', 'Username',"url","retweetCount","source","like_count","replycount","lan"]))
    df=data_frame(list_tweet)
    submit=st.checkbox("View Dataframe") 
    if submit:
          st.success("Dataframe")
          st.write(df) 

# Download scraped data as CSV or JSON file
elif choice=="Download":
    Hashtag=st.sidebar.text_input("Enter Hashtag or Keyword")
    start_date=st.sidebar.date_input("Enter starting date:(YYYY-MM-DD)")
    End_date=st.sidebar.date_input("Enter end date:(YYYY-MM-DD)")
    tweets_count=st.sidebar.number_input("Enter Tweet count",min_value=1,max_value=1500,step=2)
    tweetlist=Scrapingdata(Hashtag,start_date,End_date,tweets_count)
    def data_frame(data):
         return(pd.DataFrame(data,columns=['Datetime', 'Tweet Id', 'Text', 'Username',"url","retweetCount","source","like_count","replycount","lan"]))
    
    def convert_csv(df_input_csv):
          return df_input_csv.to_csv().encode("utf-8")

    def convert_json(j):
          return j.to_json(orient="index")

    df=data_frame(tweetlist)
    csv=convert_csv(df)
    json = convert_json(df)
    st.download_button(label="Download CSV",data=csv,file_name="file.csv",mime="text/csv") 
    st.download_button(label="Download JSON",data=json,file_name="file.json",mime="text/csv")
