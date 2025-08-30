🌍 Climate-Driven Disease Outbreak Prediction

This project explores the relationship between climate variables (temperature, humidity, precipitation) and vector-borne diseases (dengue and malaria) in India. The goal is to understand whether climate change impacts disease outbreaks and to build a foundation for predictive modeling.

📌 Project Overview

 Develop an ML model that uses climate features to predict the risk of disease outbreaks.

📊 Data Sources

The datasets used in this project were collected from reliable, open sources:

🦟 Dengue cases: OpenDengue (https://opendengue.org/)

🦟 Malaria incidence: WHO Global Health Observatory (GHO) (https://www.who.int/data/gho)  

🌡 Temperature anomalies: Berkeley Earth Surface Temperature Data (http://berkeleyearth.org/data/)  

💧 Humidity & Precipitation: World Bank Climate Change Knowledge Portal (CCKP) (https://climateknowledgeportal.worldbank.org/)  

📂 Repository Structure
Climate-Driven-Disease-Outbreak-Prediction/                                                                                                                         
│── Data/                                                                                                                                                           
│   ├── raw/               # Original raw files (downloaded datasets)                                                                                               
│   │   ├── Dengue_india.csv                                                                                                                                        
│   │   ├── malaria_indicators_ind.csv                                                                                                                              
│   │   ├── india-TAVG-Trend.txt                                                                                                                                    
│   │   ├── humidity_ind.xlsx                                                                                                                                       
│   │   ├── precipitation_ind.xlsx                                                                                                                                  
│   ├── processed/                                                                                                                                                  
│       └── India_Climate_Disease_Merged.csv   # Final cleaned dataset                                                                                              
│                                                                                                                                                                   
│── Scripts/                                                                                                                                                        
│   └── merge.py           # Data cleaning + merging script                                                                                                         
│                                                                                                                                                                   
│── sourceCodeFiles/                                                                                                                                              
│   └── main.ipynb # Jupyter Notebook for Week 1 submission                                                                                                
│                                                                                                                                                                   
│── README.md              # Project documentation                                                                                                                  
                                                                                                                                                                    
