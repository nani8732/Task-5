# 📦 Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ Load CSV
df = pd.read_csv("sales_data.csv")

# 🧾 Add a Revenue column
df["Revenue"] = df["Quantity"] * df["Price"]

# 🔍 View first few rows
print(df.head())

# 📊 1. Total Revenue by Region
region_sales = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
print("\nTotal Revenue by Region:\n", region_sales)

# 📈 Bar chart - Revenue by Region
plt.figure(figsize=(8, 5))
region_sales.plot(kind='bar', color='skyblue')
plt.title("Total Revenue by Region")
plt.ylabel("Revenue")
plt.xlabel("Region")
plt.tight_layout()
plt.show()

# 📊 2. Total Quantity Sold by Product
product_sales = df.groupby("Product")["Quantity"].sum()
print("\nTotal Quantity by Product:\n", product_sales)

# 🍩 Pie chart - Product Sales Share
plt.figure(figsize=(6, 6))
product_sales.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title("Sales Quantity Share by Product")
plt.ylabel("")
plt.tight_layout()
plt.show()

# 📊 3. Daily Revenue Trend
daily_revenue = df.groupby("Date")["Revenue"].sum()
print("\nDaily Revenue:\n", daily_revenue)

# 📅 Line plot - Revenue over time
plt.figure(figsize=(8, 5))
daily_revenue.plot(marker='o', linestyle='-', color='green')
plt.title("Revenue Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.show()
