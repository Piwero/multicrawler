import requests
import bs4


base_url = "https://www.timeout.com/london/restaurants/the-latest-top-london-restaurants-doing-home-delivery"

result = requests.get(base_url)

soup = bs4.BeautifulSoup(result.text, "lxml")

title= soup.select(".card-title")

count = 0
for item in title:
    if item:
        count += 1
        print(str(count) + ": " + item.text.strip())
