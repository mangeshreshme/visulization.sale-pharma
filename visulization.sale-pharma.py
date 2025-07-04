# Sales Visualization Project

print("Author- By Mangesh Reshme")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Loadind the data set(sales_data.csv)
df= pd.read_csv("sales_data.csv")
print(df.head())
print(df.info())
print(df.describe())
# formating Date and month in redable format
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.strftime('%b-%Y')

# 1. Visualization of Total Sales by Region(bar plot)

plt.figure(figsize=(8, 5))
region_sales = df.groupby('Region')['Sales'].sum().sort_values()
region_sales.plot(kind='barh', color='skyblue')
plt.title("Total Sales by Region")
plt.xlabel("Sales")
plt.ylabel("Region")
plt.tight_layout()
plt.show()
plt.savefig("Total Sales by Region")

# 2. Monthly Sales Trend Visualization (using Line charts)

plt.figure(figsize=(10, 5))
monthly_sales = df.groupby('Month')['Sales'].sum()
monthly_sales.plot(marker='o', color='green')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show()
plt.savefig("Monthly Sales Trend")

# 3. Product-wise Sales Distribution Visulization (Pie Chart)
plt.figure(figsize=(6, 6))
product_sales = df.groupby('Product')['Sales'].sum()
plt.pie(product_sales, labels=product_sales.index, autopct='%1.1f%%', startangle=140)
plt.title("Product-wise Sales Contribution")
plt.tight_layout()
plt.show()
plt.savefig('Product-wise Sales Contribution')

# 4. Visulization with Heatmap: Region vs Product Sales
pivot_table = df.pivot_table(index='Region', columns='Product', values='Sales', aggfunc='sum')
plt.figure(figsize=(8, 5))
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt=".0f")
plt.title("Sales by Region and Product")
plt.tight_layout()
plt.show()
plt.savefig("Sales by Region and Product")


