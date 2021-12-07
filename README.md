# YoutubeTrendingPrediction

<img src="logo/ytp_logo.png?raw=true" alt="logo" title="Title"  />

## About the project

YouTube Trending Prediction(YTP) is a Dashboard for analyzing trends and predicting YouTube trending videos through YouTube trending videos datasets. 

If you'd like to quickly preview the dashboard, you can visit our dashboard on the web: [YTP Web](https://daucheng.github.io/YTP/) 



YouTube shows all the most popular and currently trending topics all over the world which are refreshed every day. It is worthwhile to analyze these data if you want to prepare for taking new films, select recommended videos or evaluate the value of videos before collaboration. 



## Directory Structures

```
YoutubeTrendingPrediction/
  |- YoutubeTrendingPrediction/
    |- trending_tags.py
    |- __init__.py
    |- tests/
      |- test_trending_tags.py
      |- __init__.py
    |- pylintExpo/
      |- pylint_result.txt
  |- examples
    |- trending_category.ipynb
    |- trending_category.ipynb
  |- data/
    |-US_youtube_trending_data.csv
    |-US_category_id.json
    |-relatedEntities.csv
    |-relatedQueries.csv
  |- doc/
    |- FunctionalSpec.md
    |- Componentspec.md
    |- InteractionDiagram.png
    |- Technology Reviews.pdf
    |- ProjectTracking.md
    |- ProjectTracking.png
  |- logo/
    |- ytp_logo.png
  |- setup.py
  |- LICENSE
  |- README.md
```



## Datasets

The project data is in csv and json files saved in `/data`.

Source:

* [US_youtube_trending_data (2020.8 - 2021.11)](https://www.kaggle.com/rsrishav/youtube-trending-video-dataset)
* [US_category_id](https://www.kaggle.com/rsrishav/youtube-trending-video-dataset)



## Install

`git clone https://github.com/cyclopropane2019/YoutubeTrendingPrediction.git`



## Example

We have a demo notebook which will import all modules and export output for analysis. Feel free to manipulate data as you like in notebook.



## Testing

It consists of unit tests for `trending_tags.py`



Team: Bingwen Hu, Dau Cheng, Ray Wang and Xinran Wang
