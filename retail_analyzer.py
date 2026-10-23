import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class RetailAnalyzer:

    def __init__(self):
        self.df = None

    def load_data(self, file):
        try:
            df = pd.read_csv(file)
            df.columns = df.columns.str.strip()

            cols = ["Date", "Product", "Category",
                    "Price", "Quantity Sold"]

            if not all(c in df.columns for c in cols):
                print("Invalid CSV columns!")
                return

            df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
            df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
            df["Quantity Sold"] = pd.to_numeric(
                df["Quantity Sold"], errors="coerce")

            df.dropna(subset=cols, inplace=True)
            df = df[(df["Price"] >= 0) &
                    (df["Quantity Sold"] >= 0)].copy()

            if df.empty:
                print("No valid data found!")
                return

            df["Total Sales"] = df["Price"] * df["Quantity Sold"]
            self.df = df

            print("Data loaded successfully!")
            print("Total Records:", len(self.df))

        except FileNotFoundError:
            print("CSV file not found!")
        except Exception as e:
            print("Error:", e)

    def calculate_metrics(self):
        if self.df is None or self.df.empty:
            print("Load data first!")
            return

        print("\nTotal Sales:", self.df["Total Sales"].sum())
        print("Average Sales:", np.mean(self.df["Total Sales"]))

        product = self.df.groupby("Product")["Quantity Sold"].sum()
        print("Popular Product:", product.idxmax())

        daily = self.df.groupby("Date")["Total Sales"].sum().sort_index()

        if len(daily) > 1 and daily.iloc[0] != 0:
            growth = ((daily.iloc[-1] - daily.iloc[0])
                      / daily.iloc[0]) * 100
            print("Sales Growth:", round(growth, 2), "%")
        else:
            print("Sales Growth: Not available")

    def filter_data(self):
        if self.df is None or self.df.empty:
            print("Load data first!")
            return

        print("1. Filter by Category")
        print("2. Filter by Date Range")
        ch = input("Enter choice: ")

        if ch == "1":
            cat = input("Enter category: ")
            result = self.df[
                self.df["Category"].str.lower() == cat.lower()]

        elif ch == "2":
            start = pd.to_datetime(
                input("Start date (YYYY-MM-DD): "), errors="coerce")
            end = pd.to_datetime(
                input("End date (YYYY-MM-DD): "), errors="coerce")

            if pd.isna(start) or pd.isna(end) or start > end:
                print("Invalid date range!")
                return

            result = self.df[
                (self.df["Date"] >= start) &
                (self.df["Date"] <= end)]

        else:
            print("Invalid choice!")
            return

        if result.empty:
            print("No matching records!")
        else:
            print(result.to_string(index=False))

    def display_summary(self):
        if self.df is None or self.df.empty:
            print("Load data first!")
            return

        print("\n--- All Retail Records ---")
        print(self.df.to_string(index=False))

        print("\n--- Statistics ---")
        print(self.df.describe())

        print("\n--- Missing Values ---")
        print(self.df.isnull().sum())

        print("\n--- Sales by Category ---")
        print(self.df.groupby("Category")["Total Sales"].sum())

        print("\n--- Sales by Product ---")
        print(self.df.groupby("Product")["Total Sales"].sum())

    def show_charts(self):
        if self.df is None or self.df.empty:
            print("Load data first!")
            return

        self.df.groupby("Category")["Total Sales"].sum().plot(
            kind="bar", title="Sales by Category")
        plt.xlabel("Category")
        plt.ylabel("Total Sales")
        plt.tight_layout()
        plt.show()

        self.df.groupby("Date")["Total Sales"].sum().sort_index().plot(
            kind="line", marker="o", title="Sales Trend")
        plt.xlabel("Date")
        plt.ylabel("Total Sales")
        plt.tight_layout()
        plt.show()

        sns.heatmap(
            self.df[["Price", "Quantity Sold", "Total Sales"]].corr(),
            annot=True, cmap="coolwarm")
        plt.title("Sales Correlation Heatmap")
        plt.tight_layout()
        plt.show()


a = RetailAnalyzer()

print("\n--- Retail Sales Data Analyzer ---")
print("1. Load Data")
print("2. Calculate Metrics")
print("3. Filter Data")
print("4. Display Summary")
print("5. Show Charts")
print("6. Exit")

while True:
    choice = input("Enter choice: ")

    if choice == "1":
        a.load_data(input("Enter CSV file name: "))
        if a.df is not None:
            print(a.df.to_string(index=False))

    elif choice == "2":
        a.calculate_metrics()

    elif choice == "3":
        a.filter_data()

    elif choice == "4":
        a.display_summary()

    elif choice == "5":
        a.show_charts()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
