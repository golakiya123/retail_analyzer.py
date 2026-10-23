# 🛍️ Retail Sales Data Analyzer

<p align="center">
  <b>📊 A Python project to explore retail sales, calculate useful metrics, and visualize sales trends.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Analysis-Pandas%20%7C%20NumPy-2ea44f" alt="Data Analysis">
  <img src="https://img.shields.io/badge/Charts-Matplotlib%20%7C%20Seaborn-orange" alt="Charts">
</p>

## ✨ About the Project

**Retail Sales Data Analyzer** is a menu-driven Python application that reads retail sales data from a CSV file and helps analyze product performance, category sales, and sales trends.

It uses **Pandas** and **NumPy** for data processing, and **Matplotlib** and **Seaborn** to create visualizations.

## 🚀 Features

- 📂 Load and validate retail data from a CSV file
- 🧹 Clean data by converting date/numeric columns and removing invalid records
- 💰 Calculate total sales and average sales
- 🏆 Identify the most popular product by quantity sold
- 📈 Calculate sales growth when enough daily data is available
- 🔎 Filter records by product category or date range
- 📋 Display data summaries, statistics, missing values, and sales by product/category
- 📊 Visualize category sales, daily sales trends, and sales correlations

## 🧰 Built With

| Tool / Library | Purpose |
|---|---|
| Python | Application logic |
| Pandas | CSV loading, cleaning, grouping, and summaries |
| NumPy | Numerical calculations |
| Matplotlib | Bar and line charts |
| Seaborn | Correlation heatmap |

## ⚙️ Getting Started

### 1. Install the libraries

Open Command Prompt or a terminal and run:

```bash
pip install pandas numpy matplotlib seaborn
```

### 2. Add the project files

Keep these files in the same GitHub repository:

```text
retail-sales-analyzer/
├── retail_analyzer.py
├── retail_sales.csv
└── README.md
```

`retail_sales.csv` is your input dataset. Use a CSV with these column names:

```text
Date, Product, Category, Price, Quantity Sold
```

Example rows:

```csv
Date,Product,Category,Price,Quantity Sold
2026-10-01,Notebook,Stationery,50,10
2026-10-02,Pen,Stationery,20,25
2026-10-03,Bottle,Accessories,150,8
```

### 3. Run the program

```bash
python retail_analyzer.py
```

When the menu asks for a CSV file name, enter the file path, for example:

```text
retail_sales.csv
```

## 🖥️ Main Menu

```text
--- Retail Sales Data Analyzer ---
1. Load Data
2. Calculate Metrics
3. Filter Data
4. Display Summary
5. Show Charts
6. Exit
```

## 📸 Screenshots

Upload **7 screenshots** of your project to this repository. For easy setup, save them with the exact filenames shown below, then the images will appear in this README.

### 1. Main Menu
<img width="749" height="490" alt="p1" src="https://github.com/user-attachments/assets/f844602f-66db-4263-ba6a-ad5589e96e38" />


### 2. CSV Data Loaded
<img width="741" height="589" alt="p2" src="https://github.com/user-attachments/assets/f10580d9-bf3b-47b3-a5e6-77521b6ead36" />


### 3. Sales Metrics
<img width="790" height="581" alt="p3" src="https://github.com/user-attachments/assets/25a6fcb8-c84b-4dbd-9136-77e9b7ba69bc" />


### 4. Filter by Category or Date
<img width="390" height="175" alt="p4" src="https://github.com/user-attachments/assets/538969b6-c216-4183-87fe-b4f186bf5e86" />


### 5. Data Summary and Statistics
<img width="633" height="472" alt="pp5" src="https://github.com/user-attachments/assets/4605fdca-1e9d-47ec-a2e2-a62e6d16166b" />



### 6. Sales by Category Chart
<img width="633" height="473" alt="pp6" src="https://github.com/user-attachments/assets/89c59005-7f25-42d5-92c7-19f10d970843" />



### 7. Sales Trend / Correlation Heatmap
<img width="645" height="475" alt="pp7" src="https://github.com/user-attachments/assets/ff19187c-dae2-40d5-a545-44d02e499020" />



> **Tip:** Create a folder named `screenshots` in your repository and upload all seven images into it. Keep the filenames exactly as written above, or update the image paths in this README.

## 🎥 Project Demo Video

Watch the project demo here: **[Add your video link](https://example.com)**

> Replace `https://example.com` with your actual YouTube, Google Drive, or other shareable video link. Make sure the video permissions allow viewers to watch it.

## 📁 Suggested Repository Structure

```text
retail-sales-analyzer/
├── retail_analyzer.py
├── retail_sales.csv
├── README.md
└── screenshots/
    ├── screenshot-1.png
    ├── screenshot-2.png
    ├── screenshot-3.png
    ├── screenshot-4.png
    ├── screenshot-5.png
    ├── screenshot-6.png
    └── screenshot-7.png
```

## 💡 What I Practiced

- Reading and validating CSV files
- Cleaning and preparing data with Pandas
- Performing calculations and grouping data
- Using functions and a class-based structure
- Creating data visualizations
- Handling common file and input errors

## 👩‍💻 Author

**Your Name**  
*Python | Data Analysis Portfolio Project*

---

<p align="center">✨ Thanks for visiting my project! ✨</p>
