# YoutubeTrendingPrediction

<img src="logo/ytp_logo.png?raw=true" alt="logo" title="Title"  />

Team: BingWen Hu, Dau Cheng, Ray Wang and Xinrang Wang



## Background

We are mainly targeting YouTube creators, operators and advertisers. YouTube shows all the most popular and currently trending topics all over the world which are refreshed everyday. It is worthwhile to track these data everyday if you want to prepare for taking new films, select recommended videos or evaluate the value of videos before collaboration.



## Directory Structure

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



## Module Code





## Project Data

In this case, the project data is rather small, and recorded in csv files saved in `/Data`.

Datasets:

* US_youtube_trending_data (2020.8 - 2021.11)
* US_category_id

Source: https://www.kaggle.com/rsrishav/youtube-trending-video-dataset



## Example

We have a demo notebook which will import all modules and export output for analysis.



## Testing

It consists of unit tests for `trending_tags.py,`

