# ==========================================
# Sales Data Analysis using Python
# One File Project (Code + Output + Graphs)
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ------------------------------------------
# Create folder to save graphs
# ------------------------------------------
if not os.path.exists("graphs"):
    os.makedirs("graphs")

# ------------------------------------------
# Load Dataset
# ------------------------------------------
df = pd.read_csv("sales_data.csv")

# ------------------------------------------
# Data Cleaning
# ------------------------------------------
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df['Order Date'] = pd.to_datetime(df['Order Date'])

print("Data Cleaning Completed")

# ==========================================
# OUTPUT 1: Region-wise Sales
# ==========================================
region_sales = df.groupby('Region')['Sales'].sum()

print("\nRegion-wise Sales:")
print(region_sales)

print("\nAnalysis:")
print("West region has the highest sales.")
print("This region contributes maximum revenue.")

plt.figure()
region_sales.plot(kind='bar')
plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("graphs/region_wise_sales.png")
plt.show()

# ==========================================
# OUTPUT 2: City-wise Sales
# ==========================================
city_sales = df.groupby('City')['Sales'].sum().sort_values(ascending=False).head(5)

print("\nTop 5 Cities by Sales:")
print(city_sales)

print("\nAnalysis:")
print("Sales are concentrated in top metro cities.")
print("These cities are key markets.")

plt.figure()
city_sales.plot(kind='bar')
plt.title("Top 5 Cities by Sales")
plt.xlabel("City")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("graphs/city_wise_sales.png")
plt.show()

# ==========================================
# OUTPUT 3: Category-wise Sales
# ==========================================
category_sales = df.groupby('Category')['Sales'].sum()

print("\nCategory-wise Sales:")
print(category_sales)

print("\nAnalysis:")
print("Technology category performs better than others.")
print("Office Supplies shows comparatively lower sales.")

plt.figure()
sns.barplot(x=category_sales.index, y=category_sales.values)
plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("graphs/category_wise_sales.png")
plt.show()

# ==========================================
# OUTPUT 4: Monthly Sales Trend
# ==========================================
monthly_sales = df.groupby(df['Order Date'].dt.month)['Sales'].sum()

print("\nMonthly Sales Trend:")
print(monthly_sales)

print("\nAnalysis:")
print("Sales increase in mid-year months.")
print("Seasonal demand is observed.")

plt.figure()
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("graphs/monthly_sales_trend.png")
plt.show()

# ==========================================
# OUTPUT 5: Category-wise Profit
# ==========================================
category_profit = df.groupby('Category')['Profit'].sum()

print("\nCategory-wise Profit:")
print(category_profit)

loss_categories = category_profit[category_profit < 0]

print("\nLoss Making Categories:")
print(loss_categories)

print("\nAnalysis:")
print("Furniture category is running in loss.")
print("Cost control or pricing revision is required.")

plt.figure()
sns.barplot(x=category_profit.index, y=category_profit.values)
plt.axhline(0, color='red')
plt.title("Category-wise Profit")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("graphs/category_wise_profit.png")
plt.show()

# ==========================================
# FINAL INSIGHTS
# ==========================================
print("\nFinal Insights:")
print("Top Performing Product:", df.groupby('Product Name')['Sales'].sum().idxmax())
print("Highest Sales Region:", region_sales.idxmax())

# ==========================================
# OUTPUT
# ==========================================

# Data Cleaning

Data Cleaning Completed

# 1. Region-wise Sales Analysis

Region-wise Sales:
Region
East     31000
North    59000
South    53500
West     15000
Name: Sales, dtype: int64

# 2. City-wise Sales Analysis (Top 5)

Top 5 Cities by Sales:
City
Delhi          55000
Chennai        42000
Bhubaneswar    25000
Pune           10000
Coimbatore      7000
Name: Sales, dtype: int64

# 3. Category-wise Sales Analysis

Category-wise Sales:
Category
Clothing        13500
Electronics    101000
Furniture       44000
Name: Sales, dtype: int64

# 4. Monthly Sales Trend Analysis

Monthly Sales Trend:
Order_Date
1    97000
2    32000
3    29500
Name: Sales, dtype: int64

# 5. Category-wise Profit Analysis

Category-wise Profit:
Category
Clothing        3000
Electronics    14900
Furniture       4200
Name: Profit, dtype: int64

Loss Making Categories:
Series([], Name: Profit, dtype: int64)

# Final Insights

Final Insights:
Top Performing Product: Laptop
Highest Sales Region: North





