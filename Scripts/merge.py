import pandas as pd

# ---- Load datasets ----
dengue = pd.read_csv("Data/raw/Dengue_india.csv")
malaria = pd.read_csv("Data/raw/malaria_indicators_ind.csv")
temp = pd.read_csv("Data/raw/india-TAVG-Trend.txt", sep="\s+", comment="%", header=None)
humidity = pd.read_excel("Data/raw/humidity_ind.xlsx")
precipitation = pd.read_excel("Data/raw/precipitation_ind.xlsx")

# ---- Dengue ----
dengue = dengue.rename(columns={"dengue_total": "DengueCases"})
dengue = dengue[["Year", "DengueCases"]]

# ---- Malaria (incidence only) ----
malaria_clean = malaria[malaria["GHO (CODE)"] == "MALARIA_EST_INCIDENCE"]
malaria_clean = malaria_clean.rename(columns={"YEAR (DISPLAY)": "Year", "Numeric": "MalariaIncidence"})
malaria_clean = malaria_clean[["Year", "MalariaIncidence"]]

# ---- Temperature (Berkeley Earth yearly averages) ----
temp_clean = temp[[0, 1, 2]].copy()
temp_clean.columns = ["Year", "Month", "TempAnomaly"]
temp_yearly = temp_clean.groupby("Year")["TempAnomaly"].mean().reset_index()

# ---- Humidity (reshape) ----
# ---- Humidity (reshape wide -> long) ----
humidity_long = humidity.melt(var_name="YearCode", value_name="Humidity")

# Extract 4-digit years
humidity_long["Year"] = humidity_long["YearCode"].str.extract(r"(\d{4})")

# Drop rows where no year was found
humidity_long = humidity_long.dropna(subset=["Year"])

# Convert to integer
humidity_long["Year"] = humidity_long["Year"].astype(int)

# Keep only Year + Humidity
humidity_long = humidity_long[["Year", "Humidity"]]

# ---- Precipitation (annual only) ----
precip_annual = precipitation.filter(like="annual", axis=1)
precip_long = precip_annual.melt(var_name="YearCode", value_name="Precipitation")
precip_long["Year"] = precip_long["YearCode"].str.extract(r"(\d{4})").astype(int)
precip_long = precip_long[["Year", "Precipitation"]]

# ---- Merge all together ----
merged = pd.DataFrame({"Year": range(1999, 2024)})
merged = merged.merge(dengue, on="Year", how="left")
merged = merged.merge(malaria_clean, on="Year", how="left")
merged = merged.merge(temp_yearly, on="Year", how="left")
merged = merged.merge(humidity_long, on="Year", how="left")
merged = merged.merge(precip_long, on="Year", how="left")

# ---- Save final dataset ----
merged.to_csv("India_Climate_Disease_Merged.csv", index=False)
print("Final dataset saved as India_Climate_Disease_Merged.csv")
