import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

dataframe = pd.read_csv(r"C:\Users\lenovo\OneDrive\Desktop\gfg_projects\project_02\Zomato-data-.csv")

def handleRate(value):
    value = str(value).split('/')
    value = value[0]
    return float(value)

dataframe['rate'] = dataframe['rate'].apply(handleRate)

with PdfPages("zomato_analysis_plots.pdf") as pdf:
    # 1. Restaurant type countplot
    plt.figure()
    sns.countplot(x=dataframe['listed_in(type)'])
    plt.xlabel("Type of restaurant")
    plt.tight_layout()
    pdf.savefig()
    plt.close()

    # 2. Votes by restaurant type (line plot)
    grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
    result = pd.DataFrame({'votes': grouped_data})
    plt.figure()
    plt.plot(result, c='green', marker='o')
    plt.xlabel('Type of restaurant')
    plt.ylabel('Votes')
    plt.tight_layout()
    pdf.savefig()
    plt.close()

    # 3. Ratings distribution
    plt.figure()
    plt.hist(dataframe['rate'], bins=5)
    plt.title('Ratings Distribution')
    plt.tight_layout()
    pdf.savefig()
    plt.close()

    # 4. Online order countplot
    plt.figure()
    sns.countplot(x=dataframe['online_order'])
    plt.tight_layout()
    pdf.savefig()
    plt.close()

    # 5. Cost for two countplot
    plt.figure()
    sns.countplot(x=dataframe['approx_cost(for two people)'])
    plt.tight_layout()
    pdf.savefig()
    plt.close()

    # 6. Boxplot for online order vs rate
    plt.figure(figsize=(6,6))
    sns.boxplot(x='online_order', y='rate', data=dataframe)
    plt.tight_layout()
    pdf.savefig()
    plt.close()

    # 7. Heatmap
    pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
    plt.figure()
    sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d')
    plt.title('Heatmap')
    plt.xlabel('Online Order')
    plt.ylabel('Listed In (Type)')
    plt.tight_layout()
    pdf.savefig()
    plt.close()

print("✅ All plots saved in 'zomato_analysis_plots.pdf'")
