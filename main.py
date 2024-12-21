from bs4 import BeautifulSoup
import requests
response = requests.get("https://wise.com/gb/currency-converter/usd-to-kzt-rate?amount=1")
if response.status_code == 200:
 soup = BeautifulSoup(response.text,features="html.parser")
 soup_list = soup.find_all("span", {"class": "text-success"})
 item = soup_list[0].get_text(strip=True)
 exchange_rate = float(item)
 a = int(input())
 b = a * exchange_rate
 print(f"{b} ₸")
