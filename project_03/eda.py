import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr
from matplotlib.backends.backend_pdf import PdfPages

wr.filterwarnings('ignore')

df = pd.read_csv("C:\\Users\\lenovo\\OneDrive\\Desktop\\WineQT.csv")

sns.set_style("darkgrid")

# Create a PDF file to save all plots
with PdfPages("wine_EDA_report.pdf") as pdf:

    # 1️⃣ Count plot of Quality
    quality_counts = df['quality'].value_counts()
    plt.figure(figsize=(8, 6))
    plt.bar(quality_counts.index, quality_counts, color='deeppink')
    plt.title('Count Plot of Quality')
    plt.xlabel('Quality')
    plt.ylabel('Count')
    pdf.savefig()
    plt.close()

    # 2️⃣ Histograms for all numerical columns
    numerical_columns = df.select_dtypes(include=["int64", "float64"]).columns
    for feature in numerical_columns:
        plt.figure(figsize=(8, 6))
        sns.histplot(df[feature], kde=True)
        plt.title(f"{feature} | Skewness: {round(df[feature].skew(), 2)}")
        pdf.savefig()
        plt.close()

    # 3️⃣ Swarm plot
    plt.figure(figsize=(10, 8))
    sns.swarmplot(x="quality", y="alcohol", data=df, palette='viridis')
    plt.title('Swarm Plot for Quality vs Alcohol')
    pdf.savefig()
    plt.close()

    # 4️⃣ Pair plot
    sns.pairplot(df, diag_kind="kde")
    pdf.savefig()
    plt.close()

    # 5️⃣ Violin plot
    plt.figure(figsize=(10, 8))
    sns.violinplot(x="quality", y="alcohol", data=df, palette="Set2", alpha=0.7)
    plt.title('Violin Plot for Quality vs Alcohol')
    pdf.savefig()
    plt.close()

    # 6️⃣ Boxplot
    plt.figure(figsize=(10, 8))
    sns.boxplot(x="quality", y="alcohol", data=df)
    plt.title('Boxplot of Alcohol by Quality')
    pdf.savefig()
    plt.close()

    # 7️⃣ Correlation Heatmap
    plt.figure(figsize=(15, 10))
    sns.heatmap(df.corr(), annot=True, fmt='.2f', cmap='Pastel2', linewidths=2)
    plt.title('Correlation Heatmap')
    pdf.savefig()
    plt.close()

print("✅ All EDA visualizations saved in wine_EDA_report.pdf")
