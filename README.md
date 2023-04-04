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

This Data Science research project aimed to build a machine learning pipeline to predict if the first stage of the Falcon 9 lands successfully. The project involved several stages including data requirements, data collection, data wrangling, exploratory data analysis, predictive model building, and evaluation.

The data was obtained through web scraping and utilizing SpaceX API, and the preprocessing involved standardizing and organizing the landing outcomes as good and bad outcomes (1 and 0). The exploratory data analysis involved querying the data using SQL and building interactive maps with Folium and Dashboards with Dash. The predictive model was built using logistic regression, support vector machines, decision tree classifier, and K-nearest neighbors.

The major insights drawn from the EDA showed that there were more launches from the CCAFS SLC 40 site than the other two sites. The number of successful landings has increased since the first use of the launch site. There appears to be a higher success rate for landings when the payload mass is above 8000 kg, and most of the launches under 8000 kg took place at the CCAFS SLC 40 launch site. The orbit types ES-L1, GEO, HEO, and SSO have the highest success rate, and a large number of recent launches have been VLEO. The highest classification accuracy belongs to the decision tree classification model, which had a best_score_ value of 0.84214.

The project identified false positives as a major problem with the model, which could potentially be fixed by analyzing more data or using other machine learning methods. The best model with the highest accuracy was the decision tree classification model. The research project also found that the more launches SpaceX carries out, the higher their success rate, indicating that they are continuously learning and improving their rockets.

Overall, this Data Science research project successfully built a predictive model for predicting the success of the Falcon 9's first stage landing. The insights drawn from the EDA provided valuable information about the launch sites, payload mass, orbit types, and success rates. The findings could be beneficial to SpaceX in improving their rockets and ensuring successful launches in the future.



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

The machine learning model selection for this Data Science research project involved evaluating several algorithms, including logistic regression, support vector machines, decision tree classifier, and K-nearest neighbors. The decision tree classification model had the highest accuracy, with a best_score_ value of 0.84214, and was identified as the best model for predicting the success of the Falcon 9's first stage landing. False positives were noted as a significant problem with the model, which could have been resolved by analyzing more data or using other machine learning methods. Overall, the machine learning pipeline was successful in predicting the success of the Falcon 9's first stage landing, and the insights drawn from the EDA provided valuable information about the launch sites, payload mass, orbit types, and success rates that could benefit SpaceX in improving their rockets and ensuring successful launches in the future.

<p align="center">
  <img width="609" height="425" src="https://github.com/Amertastic/Applied-Data-Science-Capstone/blob/main/Images/Classification%20Accuracy.png">
</p>


### Evaluation 

The performance of the predictive models was evaluated using several metrics, including accuracy, precision, recall, and F1-score. The evaluation results showed that the decision tree classifier model had the highest classification accuracy, with a best_score_ value of 0.84214. The logistic regression and support vector machine models had lower accuracy scores, while the K-nearest neighbors model had the lowest accuracy score. The precision and recall values varied for each model, with the decision tree classifier having the highest precision score of 0.8344 and the highest recall score of 0.8548. The F1-scores were consistent with the precision and recall values, with the decision tree classifier having the highest score of 0.8445. The evaluation also identified false positives as a major problem with the models. This could potentially be fixed by analyzing more data or using other machine learning methods. Overall, the decision tree classifier model was selected as the best model for predicting the success of the Falcon 9's first stage landing based on its high accuracy and F1-score values.

### Future Work

Future work could involve collecting more data to improve the model's accuracy and reduce the false positives. It could also be beneficial to explore other machine learning algorithms, such as ensemble methods, to see if they perform better than the current models. Additionally, the model could be updated to include more recent launch data to see if there have been any changes in trends or patterns. Furthermore, it could be interesting to investigate the impact of external factors, such as weather conditions or technical issues, on the success of Falcon 9's first stage landing.
