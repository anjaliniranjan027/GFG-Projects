# 📖 Quotes Web Scraping & Data Analysis

This project demonstrates **web scraping, data cleaning, and visualization** using Python.  
It scrapes quotes from [Quotes to Scrape](http://quotes.toscrape.com/), saves them to a CSV file, and generates visualizations (Word Cloud, Tag Frequency, and Quote Length Distribution).  
All plots are combined into a single **PDF report**.

---

## 🚀 Features
- Scrapes quotes, authors, and tags from multiple pages.
- Stores data into a structured CSV file (`quotes.csv`).
- Generates:
  - ✅ Word Cloud of all quotes.
  - ✅ Top 10 most common tags (bar chart).
  - ✅ Distribution of quote lengths (histogram).
- Saves all visualizations into **one PDF file** (`quotes_visualizations.pdf`).

---

## 🛠️ Tech Stack
- **Python 3**
- **Libraries Used:**
  - `requests` – fetch web pages
  - `beautifulsoup4` – parse HTML
  - `pandas` – data handling
  - `matplotlib` – plotting
  - `seaborn` – statistical visualization
  - `wordcloud` – generate word clouds

---

## 📂 Project Structure
project_04/
│── data_analysis_web_scraping.py # Main script
│── quotes.csv # Scraped data (generated after run)
│── quotes_visualizations.pdf # PDF report with all visualizations
│── README.md # Project documentation

yaml
Copy
Edit

---

## ▶️ How to Run

1. Clone this repository or download the files.  
   ```bash
   git clone <your-repo-url>
   cd project_04
Install dependencies:

bash
Copy
Edit
pip install requests beautifulsoup4 pandas matplotlib seaborn wordcloud
Run the script:

bash
Copy
Edit
python data_analysis_web_scraping.py
Output files will be generated:

quotes.csv → scraped data

quotes_visualizations.pdf → combined report

📊 Sample Visualizations
Word Cloud of Quotes

Top 10 Tags

Distribution of Quote Lengths

(All included inside the PDF report ✅)

🎯 Learning Outcomes
Web scraping with BeautifulSoup

Handling pagination

Exporting data to CSV

Generating insights with Pandas

Creating plots with Matplotlib & Seaborn

Combining multiple plots into a single PDF report

📌 Future Improvements
Add author-specific analysis (e.g., most quoted authors)

Sentiment analysis of quotes

Interactive dashboard with Streamlit or Plotly

