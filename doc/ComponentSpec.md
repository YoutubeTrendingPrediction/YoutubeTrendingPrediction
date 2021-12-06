# Component Specification

## Component Design

*This section lists the components that we expect to have in our project (not necessarily a complete list), what they do, and how they interface (e.g., functions with inputs and outputs). This includes documentation for existing packages. For the components we have or plan to implement, we have listed the inputs and outputs.*



This project is a dashboard using Python library and Tableau. This tool is built for YouTube creators, operators and advertisers to track trending categories, tags and indivisual videos. This tool can provided predicted tendency of indivisual video leveraging machine learning package.



**Retrieve YouTube trending data using API or Kaggle**

The function runs as follows:

- Retrieves `US_category_id.json` and `US_youtube_trending_data.csv`
- Add new columns to store scores, attributes for evaluating value of trending videos
- Join two tables based on `category_id`

**Category Bubble Chart for trending topics**

Function: 

* Bubble Chart will display top 20 trending categories. 

* The area of each circle is proportional its trending score which is calculated by views, likes and dislikes.

**Word Cloud/Tag Cloud**

Function: Make a word cloud to display the trending hashtags

* Trending tags will be highlighted and their size is based on frequency, relevance and other features.
* Every tags can be clicked.

**Line Chart**

Function: To display top 10 popular videos' tendency during a period of time.

* The score, which indicates popularity of each trending videos, is calculated using a machine learning model.
* The precasted trend of each video is also displayed.
* Users will redirect to specific YouTube profile page by clicking videos tendency line.

**Control Logic** 

Machine Learning model for precasting tendency of videos and calculating score for each trending video.

* input:
* model: 
* ouput

**A Dashboard based on Github page for visualization** 

* github page(github.io)
  * css
  * html
  * Others
* Tableau
  * Line chart
  * Buble chart
  * Animation 
* Deploy Tableau on github.io 
* Others

Back-end server for retrieving datasets using provided API and update report on Dashboard (pending)

* Python code
* Using bash to upload datasets



## Interaction Diagram

![InteractionDiagram](https://mechhucloud.oss-cn-hangzhou.aliyuncs.com/uPic/InteractionDiagram.png)



## Project tracking

![image-20211205143828745](https://mechhucloud.oss-cn-hangzhou.aliyuncs.com/uPic/image-20211205143828745.png)
