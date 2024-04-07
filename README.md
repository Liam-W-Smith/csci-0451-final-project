# csci-0451-final-project

# Abstract
Our project aims to tackle the challenge of inadequate census population data in underdeveloped countries, while also providing a means to forecast populations in new developments. Leveraging landcover image data and tract geometry, our approach involves computing zonal statistics and employing a regression model. Our success will be evaluated based on the accuracy of our predictive model, thereby offering a quantitative measure of our impact in addressing the lack of population in certain areas.

# Motivation
We have very high-resolution land cover data and the population census data, and we want to connect these two data sets by seeing how land use could reflect the population in the area. Our scientific questions are: how could the machine learning algorithm be used to predict an area’s population density using the land cover type data? Which regression model performs the best at prediction? At which census scale (block, tract, or county) is the model most accurate? Our model could guide places that lack updates on census data to develop a more contextualized model to estimate population density using easier-to-acquire remote sensing data. Population census data is crucial for policymakers to understand how much necessary resources and aid a region needs. In addition, this model could be potentially used to predict population density change in newly developed suburban regions of New England. 


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

# Tentative Timeline
After 3 weeks we expect to have model with which we can make predictions. Following this, we plan to interpret our outcomes and create meaningful visualizations to display this to any audience. After 6 weeks, we will have a beautiful presentation that synthesizes our data collection, modelling, and visualizations into a cohesive story!

# Authors 
Liam W. Smith, Alex Xu, Manuel Fors

