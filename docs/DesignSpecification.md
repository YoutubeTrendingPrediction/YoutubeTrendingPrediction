# YouTubeTrends - Design Specification

## Components

*This section lists the components that we expect to have in our project (not necessarily a complete list), what they do, and how they interface (e.g., functions with inputs and outputs). This includes documentation for existing packages. For the components we have or plan to implement, we have listed the inputs and outputs.*


## Word Cloud

Tags are origanized in the style of Word Cloud and those trending ones will be in larger sizes being proportional to the total amount. In order to hightlight the more frequent ones, we only pick top 20 tags in the selected time ranges. Besides, each tag can be clicked to see videos that belong to it.


## Search Box

Below the searching bar, there are several recommanded YouTube top searching key words, which offers readers options. Furthermore, since in the aforemetioned Word Cloud, tags show up in a more random and disordered way, it is true that the diagram is more direct for readers to know what tags are more popular, but if readers want to look up for specific tags, the set of the Search Box can be a more reasonable and convenient way. In other words, it is intended as a supplement to the Word Cloud. Searching each tag, channels and videos that belongs to it will show up with corresponding amount in two seperate columns and in dscending sequence as default. 


## Line Chart

Line Chart displays popular categories in selected time ranges, it gives reader a general understanding of the past trending situation.


## Category Bubble Chart for trending prediction

We use long-short term memory (LSTM) model for precasting future videos' view counts amount and trending tendency. Bubble Chart displays trending categories in the nearest 30 days, the area of each circle is proportional to its total amount. When selecting each category, its corresponding bar charts and curve trend will show up consisting of existed view counts number and one day prediction in different colors. On top of that, not only does each category has a general prediction amount, but also specific videos in the category have.


## Interaction Diagram

![InteractionDiagram](https://mechhucloud.oss-cn-hangzhou.aliyuncs.com/uPic/InteractionDiagram.png)


## Project tracking

![image-20211205143828745](https://mechhucloud.oss-cn-hangzhou.aliyuncs.com/uPic/image-20211205143828745.png)
