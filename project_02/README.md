# 🍽 Zomato Data Analysis

This project performs an **exploratory data analysis (EDA)** on Zomato restaurant data using Python, Pandas, Matplotlib, and Seaborn.  
It generates multiple visualizations and saves them into a single PDF file for easy reference.

---

## 📌 Features
- **Data Cleaning**: Handles rating format conversion (`4.1/5` → `4.1`).
- **Exploratory Data Analysis**:
  - Distribution of restaurant types.
  - Votes comparison by restaurant type.
  - Ratings distribution.
  - Online order availability analysis.
  - Approximate cost for two people analysis.
  - Boxplot for online order vs. rating.
  - Heatmap for restaurant type vs. online order.
- **Export**: All generated plots are saved in one PDF file.

---

## 🛠️ Technologies Used
- **Python** – Core programming language
- **Pandas** – Data manipulation
- **NumPy** – Numerical operations
- **Matplotlib** – Plotting library
- **Seaborn** – Statistical data visualization

---

## 📂 File Structure
project_02/
│-- zomato_data_analysis_program.py # Main analysis script
│-- Zomato-data-.csv # Dataset
│-- zomato_analysis_plots.pdf # Output PDF with all plots


---

## 🚀 How to Run
1. **Install dependencies**:
   ```bash
   pip install pandas numpy matplotlib seaborn
2. Place the CSV file in the same folder as the Python script.
3. Run the script:
python zomato_data_analysis_program.py
4. View the results:
Open zomato_analysis_plots.pdf to see all visualizations.
│-- README.md # Project documentation

📊 Sample Visualizations
Countplot – Restaurant types
Line plot – Votes per restaurant type
Histogram – Ratings distribution
Heatmap – Restaurant type vs online order availability

📌 Notes
Ensure the CSV file name matches exactly (Zomato-data-.csv in this case).
You can change the file path in the script if your dataset is located elsewhere.
The script automatically saves plots into a multi-page PDF instead of showing them interactively.
