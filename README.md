# ETL Pipeline for Blinkit Data

## 📌 Project Overview

This project implements an **ETL (Extract, Transform, Load) pipeline** to collect and process product data from Blinkit APIs.
The pipeline extracts data from APIs, transforms it into a structured format, and loads it into a database for analysis.

## ⚙️ Tech Stack

* Python
* REST API
* Pandas
* MySQL / Database
* ETL Pipeline Architecture

## 🏗️ Project Architecture

The project follows a standard **ETL workflow**:

1. **Extract**

   * Fetch data from Blinkit APIs
   * Store raw data

2. **Transform**

   * Clean and preprocess data
   * Convert into structured format

3. **Load**

   * Insert processed data into database

## 📂 Project Structure

```
ETL-PIPELINE-FOR-BLINKIT
│
├── Extract/
├── Transform/
├── Load/
├── main.py
└── README.md
```

## ▶️ How to Run the Project

1. Clone the repository

```
git clone https://github.com/Tharanika-R-Git/ETL-PIPELINE-FOR-BLINKIT.git
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the pipeline

```
python main.py
```

## 🎯 Features

* Automated data extraction from APIs
* Data cleaning and transformation
* Database storage for further analysis
* Modular ETL architecture

## 📈 Future Improvements

* Add scheduling using Airflow or Cron
* Improve data validation
* Add dashboard for analytics

