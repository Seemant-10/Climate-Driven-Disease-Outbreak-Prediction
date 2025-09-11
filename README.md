🌍 Climate-Driven Disease Outbreak Prediction

This project explores the relationship between climate variables ( like temperature, humidity, precipitation) and vector-borne diseases (dengue and malaria) across multiple countries (120+) with monthly resolution. The goal is to explore global climate–disease patterns, identify climate risk factors for outbreaks, and build predictive ML models.

📌 Project Overview

 Develop an ML model that uses climate features to predict the risk of disease outbreaks.

📊 Data Source: 

Kaggle – Climate and Disease Dataset (https://www.kaggle.com/datasets/hopeofchange/climate-driven-disease-spread)
 (covers 120 countries, 2000–2023, monthly data).
Includes climate variables (temperature, precipitation, humidity, AQI, UV index) and disease cases (dengue, malaria).

📑 Dataset Description
| Variable                | Description                                    | Unit / Scale |
| ----------------------- | ---------------------------------------------- | ------------ |
| **year**                | Year of observation                            | YYYY         |
| **month**               | Month of observation                           | 1–12         |
| **country**             | Country name (120+ countries)                  | Categorical  |
| **region**              | Regional classification (continent/sub-region) | Categorical  |
| **avg\_temp\_c**        | Average temperature                            | °C           |
| **precipitation\_mm**   | Monthly precipitation                          | mm           |
| **air\_quality\_index** | Air Quality Index                              | AQI units    |
| **uv\_index**           | UV radiation index                             | Index        |
| **malaria\_cases**      | Reported malaria cases                         | Count        |
| **dengue\_cases**       | Reported dengue cases                          | Count        |
| **population\_density** | Population per km²                             | people/km²   |
| **healthcare\_budget**  | Healthcare budget per capita (approx.)         | USD          |


📂 Repository Structure
Climate-Driven-Disease-Outbreak-Prediction/                                                                                                                         
│── Data/                                                                                                                                                           
│   └── climate_disease_dataset                                                                                                                                                                                      
│                                                                                                                                                                   
│── sourceCodeFiles/                                                                                                                                              
│   └── main.ipynb   
|   └── app.py
|   └── random_forest_model.pkl
|   └── scaler.pkl
│                                                                                                                                                                   
│── README.md              # Project documentation                                                                                                                  
                                                                                                                                                                    
