# 🍷 Wine Quality EDA  

This project performs **Exploratory Data Analysis (EDA)** on the **Wine Quality Dataset** to uncover patterns, correlations, and insights about different chemical properties that affect wine quality.  

---

## 📂 Project Structure  
project_03/
│-- WineQT.csv # Dataset
│-- eda.py # Python script for EDA & visualizations
│-- README.md # Project documentation

## 📊 Dataset Information  

- **Dataset**: Wine Quality (WineQT.csv)  
- **Shape**: 1143 rows × 12 columns  
- **Target Variable**: `quality` (wine quality score)  

### Features:  
- Fixed Acidity  
- Volatile Acidity  
- Citric Acid  
- Residual Sugar  
- Chlorides  
- Free Sulfur Dioxide  
- Total Sulfur Dioxide  
- Density  
- pH  
- Sulphates  
- Alcohol  
- Quality (target)

---

## 🛠️ Tools & Libraries Used  

- **Python**  
- **Pandas** → Data handling  
- **NumPy** → Numerical operations  
- **Matplotlib** & **Seaborn** → Data visualizations  

---

## 📈 Visualizations Included  

1. **Count Plot of Quality**  
2. **Histograms with KDE** for all numerical features  
3. **Swarm Plot** of Alcohol vs Quality  
4. **Pair Plot** for feature interactions  
5. **Violin Plot** of Alcohol by Quality  
6. **Boxplot** of Alcohol vs Quality  
7. **Correlation Heatmap**  

All visualizations are exported into a **single PDF report** (`wine_EDA_report.pdf`) for easy review.  

---

## 🚀 How to Run  

1. Clone the repository:  
   ```bash
   git clone https://github.com/anjaliniranjan027/GFG-Projects.git
   cd project_03
Install dependencies:

bash
Copy
Edit
pip install pandas numpy matplotlib seaborn
Run the EDA script:

bash
Copy
Edit
python eda.py
Check the output PDF:

wine_EDA_report.pdf (all visualizations in one place)

📌 Insights
Higher alcohol levels are strongly correlated with better wine quality.

Certain acidity levels and sulphates also influence wine quality.

The dataset shows class imbalance (most wines have quality 5–6).

⭐ Future Improvements
Apply feature engineering for predictive modeling.

Build a classification model to predict wine quality.

Deploy results on Streamlit / Flask for interactive dashboards.

👩‍💻 Author
Anjali Niranjan
B.Tech CSE | Data Science & Analytics Enthusiast
