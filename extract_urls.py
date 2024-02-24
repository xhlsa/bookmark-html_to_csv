from bs4 import BeautifulSoup

# Open the HTML file
with open("bookmarks.html", "r", encoding="utf-8") as f:
    html_doc = f.read()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_doc, "html.parser")

# Find all anchor tags and extract their href attribute
urls = [a.get("href") for a in soup.find_all("a", href=True)]

# Save the URLs to a CSV file
with open("urls.csv", "w", encoding="utf-8") as f:
    f.write("URL\n")
    for url in urls:
        f.write(f"{url}\n")

print("URLs extracted and saved to urls.csv")
