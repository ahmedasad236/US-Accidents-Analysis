# End-to-End US-Accidents Data Pipeline

## Table of Contents
1. [Overview](#overview)
2. [Data Source](#data-source)
3. [Data Pipeline Architecture and Workflow](#data-pipeline-architecture-and-workflow)
4. [Data Engineering flow Implementation](#data-engineering-flow-implementation)
   - [MAGE](#mage)
   - [Terraform](#terraform)
   - [DBT](#dbt)
   - [Looker Studio](#looker-studio)
   - [Installation](#installation)
      - [Create GCP resource](#create-gcp-resource)
      - [Configure MAGE](#configure-mage)
      - [DBT](#dbt-1)
5. [Data Science flow Implementation](#data-science-flow-implementation)
   - [EDA](#eda)
   - [ML](#ml)
   - [Evaluation of the various Machine Learning Models](#evaluation-of-the-various-machine-learning-models)
6. [Built With](#built-with)
7. [Installing and running](#installing-and-running)
8. [Further Improvements](#further-improvements)
9. [Developers](#developers)
10. [License](#License)

## Overview

big dataset of **US accidents** from **Kaggle** to understand why accidents 
happen. We'll use different data analysis methods to find patterns in the data, like what 
makes accidents more likely in certain areas or weather conditions, and predict how severe 
can it become relative to many factors featured in the dataset. 
The **motivation** behind this idea is all about making roads safer by giving valuable 
information to people who can make a difference, like government officials, transportation 
departments, and even everyday drivers.

## Data Source 

The datasets for this project was obtained from **kaggle**. The datasets can be obtained [here](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents)

## Data Pipeline Architecture and Workflow 
![](images/us-accidents_pipeline.gif "Architecture")

The project can be divided into two sub-projects: the first is the **data engineering** project, which manages data flow, ETL orchestration, and data modeling. The second sub-project focuses on **data science**, conducting thorough exploratory data analysis (EDA) to delve into the data, extract relevant features, and implement appropriate machine learning models.


## Data Engineering flow Implementation 

#### [MAGE](https://www.mage.ai/)

MAGE is used as data orchestration to implement  **ETL** operation on us-accidents data  from kaggel load it to **Google** Cloud Storage and BigQuery

> Note : You can find more about the orchestration pipline in mage subdirectory

#### [Terraform](https://www.terraform.io/)

We utilize Terraform in GCP to provision resources including Google Cloud Storage Buckets and BigQuery datasets for efficient data management and processing.

#### [DBT](https://www.getdbt.com/)

DBT platform is employed to conduct data modeling within BigQuery, facilitating the creation of dimension and fact tables for structured and optimized data organization.

> Note : You can find more about DBT data modeing pipline  pipline in dbt  subdirectory
#### Looker Studio

Looker Studio is utilized to craft insightful dashboards showcasing statistics derived from the fact tables built through DBT, enhancing data visualization and analysis capabilities.

You can access dashboard from [here](https://lookerstudio.google.com/reporting/bca9d57c-548c-4be1-a756-b11d2473c223)
![](images/dashboard.png "dashboard")


### Installation

> To run the data flow   locally you should have the following prerequisites


- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Google Cloud SDK](https://cloud.google.com/sdk)
- [Terraform](https://www.terraform.io)
- [MAGE](https://www.mage.ai/)
- [DBT](https://docs.getdbt.com/docs/cloud/about-cloud-setup)
- [Looker Studio](https://lookerstudio.google.com)



#### Create GCP resource

> You should have a billing account in GCP

1. Create a GCP project

2. Create a service account with the following rules
   1. `Big Query Admin`
   2. `Storage Admin`
   3. `Storage Object Admin`
   4. `Viewer`
3. Download the service account credentials file to your machine
4. clone this repository

```bash
   git clone git@github.com:ahmedasad236/US-Accidents-Analysis.git
```

5. open the repo with any IDE and create a keys folder

```bash
   mkdir keys
```

6. move the credentials file to the keys folder
7. update file `terraform/variable.tf` with your credentials file path and your GCP project ID move to the `terraform` directory and run the following command

```bash
   terraform init
   terraform apply
```

8. if all the previous steps work well you should have those resources created in your GCP project


> If you get an error in Terraform, you should check if you have `terraform` installed or `terraform` in your PATH.

#### Configure MAGE

1. clone the mage repository to your machine

```bash
   git clone https://github.com/mage-ai/mage-zoomcamp
```

2. configure your service account credentials file in mage by changing `<credential file path>` in the `docker-compose.yml` file in the mage repo that you clone with the actual path in your computer

```bash
 - <credential file path>:/home/src/gcp_credentials.json
```

3. move to the mage repository and run the following command

```bash
docker-compose up -d
```

4. open this link `http://localhost:6789` in your browser
   > If you have an error with docker or docker-compose, ensure you install, docker, and docker-compose correctly and add them to your path
5. change the GCP configuration setting in mage in the `io_config.yml` file
   ![](images/io_config.png "io_config")
   change this code

```yml
# Google
... additional lines
```

to this

```yml
# Google
GOOGLE_SERVICE_ACC_KEY_FILEPATH: "/home/src/gcp_credentials.json"
GOOGLE_LOCATION: US # Optional
```

6. create a pipeline by uploading the zip file `mage/us-accidents.zip` to mage
   ![](images/upload_zip.png "upload pipeline as zip file")

7. run the pipeline, after all, pipeline blocks run you should have the 7 parquet files from `partition_2016.parquet` to `partition_2023.parquet` files in your GCP bucket, and the `accidents`  table in your BigQuery.


#### DBT

you can watch this video to understand how to create a DBT project with BigQueryConnection [dbt Cloud and BigQuery for Admins
](https://courses.getdbt.com/courses/dbt-cloud-and-bigquery-for-admins)

1. create a service account for the DBT Project with the following rules
   - `BigQuery Data Editor`
   - `BigQuery Job User`
   - `BigQuery Data Viewer`
2. download the service account key to your local machine
   > [!NOTE]
   > Before creating a dbt project fork this repo to your git hub and when creating a project choose the `dbt` folder from your fork as a subdirectory for your DBT project so you don't have to recreate models again.
3. create a DBT project with a BigQuery connection
4. run the following command in DBT Cloud IDE
   ```bash
   dbt run
   ```
5. if all steps go well all dimensions and fact tables should be created in your BigQuery dataset and you export them to Looker.



## Data Science flow Implementation

This inquiry seeks to identify the key factors and distinguishing features contributing to the Severity of the accidents. Our methodology encompasses **2** steps: 
1. Data preprocessing to ensure analytical relevance, conducting thorough Exploratory Analysis focusing on three key areas (**EDA**).
2. Applying Machine Learning techniques using Logistic regression and Random Forest.

### EDA

> For more details about code , graphs and statistics. check the following file **spark/EDA.ipynb**


### ML 

ML Models that we used for classification of the Severity are : 

1. Logistic Regression
2. Random Forrest

#### Evaluation of the various Machine Learning Models: 

| Model | Dataset | Accuracy  | F1 Score |
|---|---|---|---|
| Logistic Regression| Train | 84% | 0.768 |
| Random Forest| Train | 84% | 0.768 |

> For more details about ML models implementation  check ` spark/main.ipynb ` 


### Built With

+ [Python 3](http://www.python.org/) - Main programming language used, done in Jupyter Notebook.
+ [Pandas](https://pandas.pydata.org/) - Main library used to manipulate the datasets.
+ [Matplotlib](https://matplotlib.org/) - Used for graph plots and visualizations.
+ [Python NLTK](https://www.nltk.org/) - Used during exploratory analysis to get further insights into the textual data.
+ [Pyspark](https://spark.apache.org/docs/latest/api/python/index.html) - Distributed computing framework used for data processing and also for ML


## Further Improvements
There are many things can be improved from this project:
- Implement Logistic Regression with **MapReduce** 
- Implement **CI/CD**
- Do a comprehensive testing

##  Developers

+ [Ahmed Asaad](https://github.com/ahmedasad236)
+ [Mamdouh Attia](https://github.com/Mamdouh-Attia)

