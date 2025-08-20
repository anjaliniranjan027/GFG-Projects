import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

BASE_URL = "http://quotes.toscrape.com/"
START_PAGE = "/page/1/"

def scrape_quotes():
    quotes_data = []
    next_page = START_PAGE
    visited_pages = set()

    while next_page:
        if next_page in visited_pages:
            print(f"Detected a loop at {next_page}, exiting...")
            break
        visited_pages.add(next_page)

        url = BASE_URL + next_page
        print(f"Scraping {url}")

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        if not quotes:
            print(f"No quotes found on {url}, exiting...")
            break

        for quote in quotes:
            try:
                text = quote.find("span", class_="text").get_text(strip=True)
                author = quote.find("small", class_="author").get_text(strip=True)
                tags = [tag.get_text(strip=True) for tag in quote.find_all("a", class_="tag")]
                quotes_data.append({
                    "Quote": text,
                    "Author": author,
                    "Tags": ", ".join(tags)
                })
            except AttributeError as e:
                print(f"Error parsing quote block: {e}")
                continue

        next_btn = soup.find("li", class_="next")
        next_page = next_btn.find("a")["href"] if next_btn else None

    return quotes_data

def save_to_csv(data, filename="quotes.csv"):
    if not data:
        print("No data to save.")
        return

    try:
        with open(filename, "w", newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["Quote", "Author", "Tags"])
            writer.writeheader()
            writer.writerows(data)
        print(f"Saved {len(data)} quotes to {filename}")
    except Exception as e:
        print(f"Failed to save file: {e}")

def generate_visualizations(data, pdf_filename="quotes_visualizations.pdf"):
    with PdfPages(pdf_filename) as pdf:

        # 1️⃣ Word Cloud
        all_quotes = " ".join(data['Quote'].dropna())
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_quotes)

        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title("Word Cloud of Quotes")
        pdf.savefig()  # saves the current figure into the pdf
        plt.close()

        # 2️⃣ Top 10 Tags
        tag_counts = data['Tags'].str.split(',').explode().value_counts()
        plt.figure(figsize=(10, 6))
        tag_counts.head(10).plot(kind='barh', color='lightgreen')
        plt.title("Top 10 Most Common Tags")
        plt.xlabel("Frequency")
        plt.ylabel("Tags")
        plt.gca().invert_yaxis()
        pdf.savefig()
        plt.close()

        # 3️⃣ Quote Length Distribution
        data['Quote Length'] = data['Quote'].apply(len)
        plt.figure(figsize=(10, 6))
        sns.histplot(data['Quote Length'], bins=20, kde=True)
        plt.title('Distribution of Quote Lengths')
        pdf.savefig()
        plt.close()

    print(f"All visualizations saved to {pdf_filename}")

if __name__ == "__main__":
    scraped_data = scrape_quotes()
    save_to_csv(scraped_data)

    file_path = "quotes.csv"  # local path
    data = pd.read_csv(file_path)

    generate_visualizations(data)
