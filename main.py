import requests
from bs4 import BeautifulSoup
# put in the url to the product
url = "https://www.amazon.de/Apple-MacBook-Air-mit-Chip/dp/B08N5S9B8X/ref=asc_df_B08N5S9B8X/?tag=googshopde-21&linkCode=df0&hvadid=474028774524&hvpos=&hvnetw=g&hvrand=2195394326361437881&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9068167&hvtargid=pla-1032586151248&psc=1&th=1&psc=1"
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
            "Accept-Language": "en",
        }

amazon_html = requests.get(url=url, headers=headers).text

soup = BeautifulSoup(amazon_html, "html.parser")
price = soup.find_all(id="mbc-price-1")
price = int(str(price[0]).split()[4].replace(".", "").split(",")[0])
# put in price goal
price_goal = 1000
if price < price_goal:
    print("buy")
else:
    print("Price too high!")
