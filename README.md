# US-Accidents-Analysis

## idea:

The project will use a big dataset of US accidents from Kaggle to understand
why accidents happen. We'll use different data analysis methods to find
patterns in the data, like what makes accidents more likely in certain areas or
weather conditions, and predict how severe can it become relative to many
factors featured in the dataset.

The motivation behind this idea is all about making roads safer by giving
valuable information to people who can make a difference, like government
officials, transportation departments, and even everyday drivers.

## Dataset Link:
(49 columns – 7.7 Million records – 3 GB) ➔ [dataset link](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents)

## Planned approach:
- Understanding variables, Data cleansing (e.g.: check nulls and Default values)
– Gain insights: (e.g. Analyzing the relationship between weather conditions and accident severity, rate of accidents in cities, Map plot of severity of accidents in the US , and so on…)
- Use PySpark as a framework.
- **Descriptive analytics:**
  1. [Association Rules] ➔ find obvious correlation between differentcircumstances (e.g.: time & place of accidents)
  2. [Clustering] ➔ Accident location clusters based on latitude information.
- **Predictive analytics:**
  1. [classification]➔ Predicting the severity of an accident based on the factors involved.
  2. [Regression]➔ Predicting accident Duration as indicator of impact on traffic flow.
- Algorithms to be implemented using **MapReduce** : Linear regression.
