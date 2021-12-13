# YouTubeTrends - Design Specification

# COMPONENTS

*This section lists the components that we expect to have in our project (not necessarily a complete list), what they do, and how they interface (e.g., functions with inputs and outputs). This includes documentation for existing packages. For the components we have or plan to implement, we have listed the inputs and outputs.*


## Category Bubble Chart for trending topics 

* Bubble Chart displays top 20 trending categories. The area of each circle is proportional to its trending score which is calculated by the amount of views, likes and trending days.

* There is a filter beside so that the reader can choose different time range, such as a specific date or the average number of a month.

## Word Cloud/Tag Cloud

* Tags are origanized in the style of Word Cloud and trending ones will be highlighted, as well as their size are based on frequency.

* Every tag can be clicked to see detailed information.


## Line Chart

* Line Chart will display the top 10 popular videos' tendency in a period of time.

* Scores can indicate popularity of each trending videos, wchih are calculated by using machine learning..


## Trending Prediction Model

Long short term memory (LSTM) model for precasting future videos' view counts and trending tendency.

* Input: video category
* Model: `TensorFlow` LSTM and `scipy` interpolate
* Ouput: A dictionary containing trending videos in the past 5 days and their predicted view counts as well as the trending tendency of one day in advance.

## A Dashboard based on Github page for Visualization

* Github page(github.io)
  
  * css
  
  * html
  
  * Others

* Tableau
  
  * Line charts
  
  * Bubble charts
  
  * Animation 

* Deploy Tableau on github.io 


* Back-end server for retrieving datasets using provided API and update report on Dashboard (pending)

  * Python code

  * Using bash to upload datasets


## Interaction Diagram

![InteractionDiagram](https://mechhucloud.oss-cn-hangzhou.aliyuncs.com/uPic/InteractionDiagram.png)


## Project tracking

![image-20211205143828745](https://mechhucloud.oss-cn-hangzhou.aliyuncs.com/uPic/image-20211205143828745.png)
