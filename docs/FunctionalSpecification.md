# Functional Specification

## Background

YouTube is a worldwide platform that can show the most popular and currently trending videos updating everyday, which means that it is worthwhile to track these data if wanting to prepare for making new vidoes, selecting recommended topics and evaluating the value of videos before collaboration.Thus, it is obvious that we are targeted at YouTubers and sponsors.


## User profile

* YouTubers:
The YouTubers will interact with this tool by understanding what kind of topics are most popular these days. The tool will show them the categories and tags that have the highest amount of view counts in the time periods they select, which can be days and months. A statistical model will be built from this data and used to predict the tendancy of topics becoming more or less popular. Besides, they can click at topics that they want to explore to see the current situation in details.Thus, they can produce their own videos based the information gathered by this tool.

* Sponsors: 
Sponsors will search for popular YouTube channels whose topics can connect well with their products so that they can find the most suitable influencers to work with. The value of ads is also an imperative part when choosing channels which means the channel's video can be popular for several days.


## User background knowledge

Both these users do not need to have knowledge of programming like python or git because our app is based on the Web.


## User Cases

Youtubers:
A YouTuber wants to search trending videos which are related to his domain and retrieves respective views count, likes count and dislikes count. Given the real-time tendency of each topics, he also wants to know predicted tendency in the future.

   **Dashboard**: Displays hottest hashtags in word cloud
   **User**: Choose time range and click on a hashtag on the screen to see videos under the tag
   **Dashboard**: Offers a search box to search tags and gives recommanded key words
   **User**: Type in the tag name in the search box and can see the trending channels and videos that under the tag
   **Dashboard**: Display the trending categories in line chart
   **User**: Choose time ranges and categories by clicking filters on the screen to see the specific amount at specific times
   **Dashboard**: Showing videos tendency in bubble chart and line chart
   **User**: Click on the interested category to see corresponding view counts changing curve
   **Dashboard**: Showing the prediction and related information of the video.
   **User**: Learning what happened on the Internet and jump on the bandwagon.


Sponsors:
A sponsor wants to know the hottest trend or category. Given the hashtags of trend videos, he wants to link their products with the hottest trend and finds the most suitable influencers to work with. He also wants to valuate the value of the ads using key features of the video(viewers, likes, dislikes) 

   **Dashboard**: Displaying the top 20 trending categories in a buble chart
   **User**: Click on a trending category on the screen they are most interested in
   **Dashboard**: Displaying hottest hashtags in a word cloud
   **User**: Click on a hashtag on the screen they are most interested in
   **Dashboard**: Showing the top 10 videos tendency(evaluate them with score) with specific category and tag during several days.
   **User**: Click on a video tendency line
   **Dashboard**: Showing the video profile and redircting to their webpage
