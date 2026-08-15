# Global Retail Sales Performance & Profitability Analysis

## Project Overview

This project analyzes global retail sales data to identify sales trends, profitability drivers, customer behavior, regional performance, and the impact of discounts on business profitability.

The project uses Python and Exploratory Data Analysis (EDA) techniques to transform raw retail data into meaningful business insights and recommendations.

## Objectives

- Analyze overall sales and profitability
- Identify high-performing categories and sub-categories
- Analyze regional and yearly sales performance
- Study the relationship between discounts and profit
- Identify the most profitable and loss-making products
- Analyze customer segments, shipping modes, and order priorities
- Generate actionable business recommendations

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- VS Code
- Git & GitHub

## Key KPIs

| KPI | Value |
|---|---:|
| Total Sales | 3,075,011 |
| Total Profit | 577,692.29 |
| Total Quantity Sold | 69,449 |
| Overall Profit Margin | 18.79% |
| Records Analyzed | 20,067 |
| Years Covered | 2011–2014 |

## Key Insights

- Technology achieved the highest profit margin among the major categories at **25.18%**.
- Furniture had the lowest category profit margin at **11.72%**.
- Sales increased from **551,280 in 2011** to **1,035,005 in 2014**.
- Overall profit margin decreased from **20.59% in 2011** to **17.07% in 2014**.
- Higher discount levels were associated with significant reductions in profitability.
- Several products generated substantial losses and require further pricing and discount review.

## Business Recommendations

- Focus on high-performing Technology products.
- Review pricing and discount strategies for Furniture.
- Avoid excessive discounts that negatively affect profitability.
- Investigate loss-making products before increasing their promotion.
- Monitor profit margin along with sales growth.

## Project Structure

```text
Global_Retail_Sales_Analysis/
│
├── data/
│   ├── SuperStore_Orders.csv
│   ├── cleaned_superstore_orders.csv
│   └── data_cleaned.csv
│
├── notebooks/
│   └── sales_analysis.ipynb
│
├── outputs/
│   └── charts/
│
├── src/
│   └── data_cleaning.py
│
└── README.md