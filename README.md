# csci-0451-final-project

# Abstract
Our project aims to tackle the challenge of inadequate census population data in underdeveloped countries, while also providing a means to forecast populations in new developments. Leveraging landcover image data and tract geometry, our approach involves computing zonal statistics and employing a regression model. Our success will be evaluated based on meeting our deliverables. However the success of our model will be based on its accuracy, thereby offering a quantitative measure of our impact in addressing the lack of population in certain areas.

# Motivation
We have very high-resolution land cover data and the population census data, and we want to connect these two data sets by seeing how land use could reflect the population in the area. Our scientific questions are: how could the machine learning algorithm be used to predict an area’s population density using the land cover type data? Which regression model performs the best at prediction? At which census scale (block, tract, or county) is the model most accurate? Our model could guide places that lack updates on census data to develop a more contextualized model to estimate population density using easier-to-acquire remote sensing data. Population census data is crucial for policymakers to understand how much necessary resources and aid a region needs. In addition, this model could be potentially used to predict population density change in newly developed suburban regions of New England. 

# Planned Deliverables

# Resources Required
Our data sources are a landcover dataset published by CONUS that 

We downloaded tract geometries directly into our Jupyter Notebook using the Pygris package.
Finally, we downloaded the total population for each census tract within Connecticut from Social Explorer, which is available [here](data/population.csv).
The first step of our data preparation will be to calculate the proportion of pixels within each tract that are each landcover class.
This type of operation is known as a Zonal Statistic in GIS, and might be a computationally expensive operation on our 800 MB image.
We may require additional computational power to make that operation work, but we do not anticipate the rest of our work requiring more computational effort than our personal computers can handle.


# What will we learn?
Alex: Most of the GIS work was on GIS software. I would like to take advantage of this project to expose myself to using GIS in a Python environment. More specifically, I will learn how to work on geographical data cleaning, aggregation, and zonal statistics in Python. From a machine learning perspective, I would like to practice implementing a regression model. 

Manny: I am learning a whole new application of CS, GIS! This is super interesting and I am taking this chance to explore how to use my current CS skills to a GIS workflow. I will implmement zonal statistics and clean geographical data as well as implement a regression model. By implmementing the regression model, I satisfy my goal of developing more theoretically and mathematically. 
# Risk Statement
Computational power could result in a potential failure to reach full deliverables. 

# Ethics Statement
We are implementing this project with the expectation that it can assist policy-makers and humanitarian aid reach the right groups of people regardless of strong census data. This data is particularly applicable to areas in the Northeast with similar geography and population dynamics as Connecticut. While the US has very cohesive census data, this can also serve as a prediction for areas yet to be developed. However, we are also aware that this data is extremely Northeast US-centric. This means that our initial intent of this model being used to predict population of areas beyond the US may fail. While the intent is not exclusionary, it may negatively affect those populations by incorrectly predicting census data. 
We do believe the world will be an overall better place following this model. Our assumptions are that population can be predicted based on satellite data, and that by accurately predicting population, policy makers and humanitarian aid can function more cohesively without the need for substantial census data.

# Tentative Timeline
After 3 weeks we expect to have model with which we can make predictions. Following this, we plan to interpret our outcomes and create meaningful visualizations to display this to any audience. After 6 weeks, we will have a beautiful presentation that synthesizes our data collection, modelling, and visualizations into a cohesive story!

# Authors 
Liam W. Smith, Alex Xu, Manuel Fors

