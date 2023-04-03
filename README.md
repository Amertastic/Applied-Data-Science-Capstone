# IBM Applied-Data-Science-Capstone
Applied Data Science Capstone For The IBM Data Science Professional Certificate [Achieved 100%]





<p align="center">
  <img width="150" height="150" src="https://github.com/Amertastic/Applied-Data-Science-Capstone/blob/main/Images/Applied%20Data%20Science%20Capstone.png?raw=true">
</p>

<!---
<img src="https://images.credly.com/size/340x340/images/798cd889-5828-4b7b-ace4-81ecb79201de/image.png" width="200" height="200">
#![IBM Applied Data Science Capstone](https://images.credly.com/size/340x340/images/798cd889-5828-4b7b-ace4-81ecb79201de/image.png)
--->

## Table of Contents

1) Navigating the Git Hub Repository
2) Executive Summary
3) Technologies and Libraries Used
4) Data Cleaning Data Gathering and Feature Engineering
5) Modelling
6) Evaluation

### Navigating the GitHub Repository

- Jupyter Notebooks: The main Jupyter Notebooks can be found in the Notebooks folder.
  - 01 Data Collection API.ipynb
  - 02 Webscraping.ipynb
  - 03 Data wrangling.ipynb
  - 04 EDA with SQL.ipynb
  - 05 EDA Using Pandas and Matplotlib.ipynb
  - 06 Interactive Visual Analytics with Folium.ipynb
  - 07 SpaceX Machine Learning Prediction.ipynb
- Data: The relevant CSV files can be found in the Data Folder.
  - dataset_part_1.csv
  - dataset_part_2.csv
  - dataset_part_3.csv
  - spacex_web_scraped.csv
- Presentation: Folder for presentation of the project.
  - Data Science Capstone Presentation.pptx.pdf
- README.md

### Executive Summary

This data science research project aimed to build a machine learning pipeline to predict the success of the first stage landing of SpaceX Falcon 9 rockets. The project involved several stages, including data collection through web scraping and utilizing SpaceX API, data preprocessing, exploratory data analysis using various tools such as Folium, Dash, and SQL, model building using four different algorithms, and model evaluation using train-test split and grid search techniques.

The analysis of the data showed that the KSC LC-39A launch site had the highest number of successful launches, and the success rate of launches increased significantly between 2013-2014 and 2015-2017. Moreover, the success rate was higher for orbit types such as ES-L1, GEO, HEO, and SSO. Payload mass and launch site also had an impact on the success rate of the launches.

The models built using logistic regression, support vector machines, decision tree classifier, and k-nearest neighbors had an R^2 error or .score() value of 0.83333. The decision tree model had the highest accuracy score of 0.84214, and it was identified as the best model among the four algorithms analyzed. However, all models had issues with false positives.

Overall, this project suggests that SpaceX's success rate is improving with each launch, and they are continuously learning from their mistakes to improve their rockets. The study also highlights the importance of data analysis in predicting the success of space missions. Further analysis and more data may help improve the accuracy of the predictive models and overcome the false positives issue.

In conclusion, this data science research project provides valuable insights and recommendations for SpaceX and the space industry as a whole to improve the success rate of space missions.


### Technologies and Libraries Used

 - Python
 - Numpy
 - Pandas
 - Matplotlib
 - Seaborn
 - Scikit-learn
 - Folium 
 - Plotly Dash
 - SpaceX REST API



### Data Collection Overview

Overview for this project involved obtaining SpaceX launch data using the SpaceX REST API. The API provided information about past launches, including rocket used, payload delivered, launch and landing specifications, and landing outcomes. A get request was made using the requests library to obtain the launch data, which was then converted into a JSON format using the .json() method. The JSON data was then normalized using the json_normalize function to convert it into a flat table format, suitable for further analysis. In addition to the API, the Python BeautifulSoup package was used for web scraping related Wiki pages to gather Falcon 9 launch records, which were then parsed and converted into a Pandas data frame for analysis.


### Data Wrangling 

During the Data Wrangling process, the gathered data was transformed into a clean dataset that provided meaningful data on the situation being addressed. This involved addressing issues such as null values and filtering out Falcon 1 launches. Identification numbers were also converted into actual data by using the API to target specific endpoints to gather data for each ID number. Null values in the PayloadMass column were replaced with the mean, while the LandingPad column with null values was left as is and dealt with later using one hot encoding. The end result was a clean and structured dataset suitable for further analysis and modeling.

<p align="center">
  <img src="https://camo.githubusercontent.com/9141210ace06c3858dcd22dbb06deefbe8a5f65c973b2248b91a04f8e1081bf9/68747470733a2f2f63662d636f75727365732d646174612e73332e75732e636c6f75642d6f626a6563742d73746f726167652e617070646f6d61696e2e636c6f75642f49424d446576656c6f706572536b696c6c734e6574776f726b2d445330373031454e2d536b696c6c734e6574776f726b2f6170692f496d616765732f6c616e64696e675f312e676966">
</p>

<!---
![](https://camo.githubusercontent.com/9141210ace06c3858dcd22dbb06deefbe8a5f65c973b2248b91a04f8e1081bf9/68747470733a2f2f63662d636f75727365732d646174612e73332e75732e636c6f75642d6f626a6563742d73746f726167652e617070646f6d61696e2e636c6f75642f49424d446576656c6f706572536b696c6c734e6574776f726b2d445330373031454e2d536b696c6c734e6574776f726b2f6170692f496d616765732f6c616e64696e675f312e676966)
--->

### Machine Learning Model Selection


### Future Work

Future work could involve collecting more data to improve the model's accuracy and reduce the false positives. It could also be beneficial to explore other machine learning algorithms, such as ensemble methods, to see if they perform better than the current models. Additionally, the model could be updated to include more recent launch data to see if there have been any changes in trends or patterns. Furthermore, it could be interesting to investigate the impact of external factors, such as weather conditions or technical issues, on the success of Falcon 9's first stage landing.
