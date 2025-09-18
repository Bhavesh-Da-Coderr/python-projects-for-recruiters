import requests
from bs4 import BeautifulSoup
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

URL = "https://realpython.github.io/fake-jobs/"

def scrape_jobs(url=URL):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    job_titles = [h2.get_text() for h2 in soup.find_all("h2", class_="title")]
    return job_titles

def analyze_jobs(job_titles):
    words = " ".join(job_titles).split()
    common = Counter(words).most_common(10)
    print("\nTop words in job titles:", common)

    wc = WordCloud(width=600, height=400, background_color="white").generate(" ".join(job_titles))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    print("🔎 Scraping jobs...")
    jobs = scrape_jobs()
    print(f"Found {len(jobs)} job titles.")
    analyze_jobs(jobs)
