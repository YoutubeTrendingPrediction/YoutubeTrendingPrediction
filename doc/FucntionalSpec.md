# Functional Specification

## Background

We are mainly targeting YouTube creators, operators and advertisers. YouTube shows all the most popular and currently trending topics all over the world which are refreshed everyday. It is worthwhile to track these data everyday if you want to prepare for taking new films, select recommended videos or evaluate the value of videos before collaboration.



## User profile

 There are a few people that might be our potential users who can benefit from our app:

1. YouTube creators are seeking a tool to track the most popular videos and genres at the moment in order to grow their channels. This tool is capable to give creators a peek into what is currently popular and might be in the future. This app allows them to leverage a particular topic to reach out and connect to the most amount of viewers.
2. An advertiser is searching for popular YouTube channels whose topics link their products well so that she can find the most suitable content creators to work with. The value of ads is also an imperative part when choosing channels which means the channel's video can be popular for several days.

All these users do not have knowledge of programming like python or git because our app is based on the Web.



## Data Sources

Datasets:

* US_youtube_trending_data (2020.8 - 2021.11)
* US_category_id

Source: https://www.kaggle.com/rsrishav/youtube-trending-video-dataset



## Use Cases

1. A YouTube creator wants to search top 10 trends videos which are related to his domain and retrieve respective views count, likes count and dislikes count. Given the real-time tendency of each topics, he also wants to know predicted tendency in the future.

   **Dashboard**: Displaying the top 20 trending categories in a buble chart
   **User**: Click on a trending category on the screen they are most interested in

   **Dashboard**: Displaying hottest hashtags in a word cloud

   **User**: Click on a hashtag on the screen they are most interested in

   **Dashboard**: Showing the top 10 videos tendency(evaluate them with score) with specific category and tag during several days.
   **User**: Click on the prediction button
   **Dashboard**: Showing the prediction and related info of the video. (Related/Similar trending Video, People who might interest, Value of the video)

   **User**: Learning what happened on the Internet and jump on the bandwagon.

   [User: (After making their video) Types some keywords about their creation.
   Dashboard: Show system the prediction and related info of the video. (Related/Similar trending Video, People who might interest, Value of the video)] pending

   

2. The advertiser wants to know the hottest trend or category. Given the hashtags of trend videos, she wants to link their products with the hottest trend and find the most suitable content creators to work with. She also wants to valuate the value of the ads using key features of the video(viewers, likes, dislikes) 

   **Dashboard**: Displaying the top 20 trending categories in a buble chart
   **User**: Click on a trending category on the screen they are most interested in

   **Dashboard**: Displaying hottest hashtags in a word cloud

   **User**: Click on a hashtag on the screen they are most interested in

   **Dashboard**: Showing the top 10 videos tendency(evaluate them with score) with specific category and tag during several days.

   **User**: Click on a video tendency line

   **Dashboard**: Showing the video profile and redircting to their webpage

   

