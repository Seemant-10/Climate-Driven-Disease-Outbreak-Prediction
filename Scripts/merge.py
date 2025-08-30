import pandas as pd
import calendar

# ---- Load datasets ----
dengue = pd.read_csv("Data/raw/Dengue_india.csv")
malaria = pd.read_csv("Data/raw/malaria_indicators_ind.csv")
temp = pd.read_csv("Data/raw/india-TAVG-Trend.txt", sep="\s+", comment="%", header=None)
humidity = pd.read_csv("Data/raw/humidity_india_monthly_complete.csv")
precip_monthly = pd.read_csv("Data/raw/precipitation_india.csv")  

# ---- Dengue (duplicate yearly into months) ----
dengue = dengue.rename(columns={"dengue_total": "DengueCases"})
dengue = dengue[["Year", "DengueCases"]]
dengue = dengue.loc[dengue.index.repeat(12)].reset_index(drop=True)
dengue["Month"] = list(range(1, 13)) * (len(dengue) // 12)

# ---- Malaria (duplicate yearly into months) ----
malaria_clean = malaria[malaria["GHO (CODE)"] == "MALARIA_EST_INCIDENCE"]
malaria_clean = malaria_clean.rename(columns={"YEAR (DISPLAY)": "Year", "Numeric": "MalariaIncidence"})
malaria_clean = malaria_clean[["Year", "MalariaIncidence"]]
malaria_clean = malaria_clean.loc[malaria_clean.index.repeat(12)].reset_index(drop=True)
malaria_clean["Month"] = list(range(1, 13)) * (len(malaria_clean) // 12)

# ---- Temperature (Berkeley Earth monthly anomalies) ----
temp_clean = temp[[0, 1, 2]].copy()
temp_clean.columns = ["Year", "Month", "TempAnomaly"]

# ---- Humidity (from the new CSV file) ----
# Keep only the row that contains actual data (row with _key = "data")
humidity_data = humidity[humidity["_key"] == "data"]

# Drop metadata columns
humidity_data = humidity_data.drop(columns=["_key", "apiVersion", "status"])

# Melt into Year-Month format
humidity_long = humidity_data.melt(var_name="YearMonth", value_name="Humidity")

# Extract Year and Month from "IND/YYYY-MM"
humidity_long["Year"] = humidity_long["YearMonth"].str.extract(r"IND/(\d{4})").astype(int)
humidity_long["Month"] = humidity_long["YearMonth"].str.extract(r"-(\d{2})").astype(int)

humidity_long = humidity_long[["Year", "Month", "Humidity"]]

# ---- Precipitation (reshape wide -> long) ----
# Keep only the row that contains actual data (row with _key = "data")
precip_data = precip_monthly[precip_monthly["_key"] == "data"]

# Drop metadata columns
precip_data = precip_data.drop(columns=["_key", "apiVersion", "status"])

# Melt into Year-Month format
precip_long = precip_data.melt(var_name="YearMonth", value_name="Precipitation")

# Extract Year and Month from "monthly/IND/YYYY-MM"
precip_long["Year"] = precip_long["YearMonth"].str.extract(r"(\d{4})").astype(int)
precip_long["Month"] = precip_long["YearMonth"].str.extract(r"-(\d{2})").astype(int)

precip_long = precip_long[["Year", "Month", "Precipitation"]]

# ---- Merge all together ----
merged = temp_clean.merge(dengue, on=["Year", "Month"], how="left")
merged = merged.merge(malaria_clean, on=["Year", "Month"], how="left")
merged = merged.merge(humidity_long, on=["Year", "Month"], how="left")
merged = merged.merge(precip_long, on=["Year", "Month"], how="left")

# Filter to 2000–2023
merged = merged[(merged["Year"] >= 2000) & (merged["Year"] <= 2023)]

# ---- Save final dataset ----
merged.to_csv("India_Climate_Disease_Merged_Monthly.csv", index=False)
print("Final dataset saved as India_Climate_Disease_Merged_Monthly.csv")
