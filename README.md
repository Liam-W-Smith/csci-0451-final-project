# csci-0451-final-project

# Abstract
Our project aims to tackle the challenge of inadequate census population data in underdeveloped countries, while also providing a means to forecast populations in new developments. Leveraging landcover image data and tract geometry, our approach involves computing zonal statistics and employing a regression model. Our success will be evaluated based on meeting our deliverables. However, the success of our model will be based on its accuracy, thereby offering a quantitative measure of our impact in addressing the lack of population in certain areas.

# Motivation
There was a webinar called “Humanitarian Applications Using NASA Earth Observations” presented by NASA about how satellite remote-sensing data could be useful in monitoring humanitarian conditions at refugee settlements. Human settlements could be detected through remote sensing images and therefore could be used to predict the population in a region. This talk alerts us that people still lack plenty of necessary population data in many parts of the world, but also demonstrates to us how remote sensing could be a powerful tool in tackling this problem and merging the data voids. We would like to explore how useful is remote sensing data in predicting the population. Given the limited time available to implement the project and the difficulty of acquiring ground-truth data in certain parts of the world, we decided to investigate how we could potentially build the connection between remote sensing land cover data and population density in a context with better data coverage. 

We have very high-resolution land cover data on the coastal states of the United States and the national population census data, and we want to build a connection between these two data sets using machine learning models. Our scientific questions are: how could the machine learning algorithm be used to predict an area’s population density using the land cover type data? Which regression model performs the best at prediction? At which census scale (block, tract, or county) is the model most accurate? Our model could guide places that lack updates on census data to develop a model to estimate population density using easier-to-acquire remote sensing data. Population census data is crucial for policymakers to understand how much necessary resources and aid a region needs. In addition, this model could be potentially used to predict population density change in newly developed suburban regions of New England.


# Planned Deliverables
* Code explaining our data collection process
* A jupyter notebook showcasing our package to analyze data
### Full success 

### Partial success


# Resources Required
Our first data source is 1-meter resolution landcover imagery covering the entire state of Connecticut.
Derived from NAIP, the data has already been processed such that every pixel represents a certain class of landcover.
At over 800 MB, the dataset is too large to share via GitHub, but you can download it yourself by clicking on the first option at [this link](https://coastalimagery.blob.core.windows.net/ccap-landcover/CCAP_bulk_download/High_Resolution_Land_Cover/Phase_2_Expanded_Categories/Legacy_Land_Cover_pre_2024/CONUS/index.html).

Our other data sources are the geometries and population data on the Census tract level for the state of Connecticut.
We downloaded tract geometries directly into [our Jupyter Notebook](code/final_project.ipynb) using the Pygris package, and we downloaded the population data from Social Explorer, storing it [here](data/population.csv).
The first step of our data preparation will be to calculate the proportion of pixels within each tract that are each landcover class.
This type of operation is known as a Zonal Statistic in GIS, and might be a computationally expensive operation on our 800 MB image.
We may require additional computational power to make that operation work, but we do not anticipate the rest of our work requiring more computational effort than our personal computers can handle.


# What will we learn?
Alex: Most of my GIS work was implemented on GIS software. I would like to take advantage of this project to expose myself to using GIS in a Python environment. More specifically, I will learn how to work on geographical data cleaning, aggregation, and zonal statistics in Python. From a machine learning perspective, I would like to practice implementing a regression model. 

Manny: I am learning a whole new application of CS, GIS! This is super interesting and I am taking this chance to explore how to use my current CS skills to a GIS workflow. I will implement zonal statistics and clean geographical data as well as implement a regression model. By implementing the regression model, I satisfy my goal of developing more theoretically and mathematically. 

Liam: I will use this project as an opportunity to learn how to implement a regression model from scratch and apply it to a geographic context. I will improve my theoretical machine-learning skills as well as my ability to apply machine learning-to spatial datasets. This will satisfy my goals of growing my knowledge of machine learning theory and implementation, as well as my desire to apply remote sensing to spatial remote sensing data.

# Risk Statement
One potential risk is that we will not have enough computational power to compute the zonal statistic on our personal computers, failing to obtain the input data for our model.
There is also some uncertainty regarding the degree to which land cover can predict population, so it is possible that our model will not perform particularly well.

# Ethics Statement
We are implementing this project with the expectation that it can assist policy-makers and humanitarian aid to reach the right groups of people regardless of strong census data. This data is particularly applicable to areas in the Northeast with similar geography and population dynamics as Connecticut. While the US has very cohesive census data, this can also serve as a prediction for areas yet to be developed. However, we are also aware that this data is extremely Northeast US-centric. This means that our initial intent of this model being used to predict the population of areas beyond the US may fail. While the intent is not exclusionary, it may negatively affect those populations by incorrectly predicting census data. 
We do believe the world will be an overall better place following this model. Our assumptions are that population can be predicted based on satellite data and that by accurately predicting population, policymakers and humanitarian aid can function more cohesively without the need for substantial census data.

# Tentative Timeline
After 3 weeks we expect to have a model with which we can make predictions. Following this, we plan to interpret our outcomes and create meaningful visualizations to display this to any audience. After 6 weeks, we will have a beautiful presentation that synthesizes our data collection, modeling, and visualizations into a cohesive story!

# Authors 
Liam W. Smith, Alex Xu, Manuel Fors

