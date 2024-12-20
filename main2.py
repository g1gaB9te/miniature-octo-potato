from bs4 import BeautifulSoup
import requests
response = requests.get("https://www.ventusky.com/astana")
if response.status_code == 200:
 soup = BeautifulSoup(response.text,features="html.parser")
 soup_list = soup.find_all("td", {"class": "temperature"})
 for item in soup_list:
  print(item.get_text(strip=True))
 soup_list2= soup.find_all("h1")
 for item2 in soup_list2:
     print(item2.get_text(strip=True))
import datetime
import sqlite3
current_time = datetime.datetime.now()
connection = sqlite3.connect("itstep_DB.sl3")
cur = connection.cursor()
cur.execute(f"INSERT INTO first_table (temperature) VALUES ('{item.get_text(strip=True)}');")
cur.execute(f"INSERT INTO first_table (time) VALUES ('{current_time}');")
connection.commit()
connection.close()