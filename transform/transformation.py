import pandas as pd
import os

# read latest raw file
raw_folder = "../data/raw"

files = os.listdir(raw_folder)

latest_file = sorted(files)[-1]

file_path = f"{raw_folder}/{latest_file}"

df = pd.read_csv(file_path)

print("Loaded file:", latest_file)

# remove duplicates
df = df.drop_duplicates()

# remove rows where product name is missing
df = df.dropna(subset=["name"])

# convert price columns to numeric
df["mrp"] = pd.to_numeric(df["mrp"], errors="coerce")
df["selling_price"] = pd.to_numeric(df["selling_price"], errors="coerce")

# create processed folder if it doesn't exist
os.makedirs("../data/processed", exist_ok=True)

# save clean data
df.to_csv("../data/processed/clean_productsnew.csv", index=False)

print("Transformation completed successfully")