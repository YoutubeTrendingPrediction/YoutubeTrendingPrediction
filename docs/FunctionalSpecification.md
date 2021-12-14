# Functional Specification

## Background

YouTube is a worldwide platform that can show the most popular and currently trending videos updating everyday, which means that it is worthwhile to track these data if wanting to prepare for making new vidoes, selecting recommended topics and evaluating the value of videos before collaboration.Thus, it is obvious that we are targeted at YouTubers and sponsors.


## User profile

* YouTubers:
The YouTubers will interact with this tool by understanding what kind of topics are most popular these days. The tool will show them the top 20 categories and tags that have the highest number of viewing in the time peirod they select. The time peirod can be days and months. A statistical model will be built from this data and used to predict the tendancy of topics becoming more or less popular. Besides, they can click at topics that they want to explore to see the current situation in details. The tool offers the proportion of different kinds of comments and the time period in a day that this topic trends, which tells influencers what aspects the audience have more interest in or some areas remain undeveloped and can be explored. Influencers can adjust their video content or change key points to make their videos stand out.
In order to make their own videos, YouTubers are seeking for a tool which can show the most popular genres at the present and can offer them a peek into what can stay populur in the near future, allowing them to leverage a particular topic to reach out and connect to the most amount of viewers.
* An advertiser is searching for popular YouTube channels whose topics link their products well so that she can find the most suitable content creators to work with. The value of ads is also an imperative part when choosing channels which means the channel's video can be popular for several days.

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

   

