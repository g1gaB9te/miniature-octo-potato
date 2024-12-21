import requests
from bs4 import BeautifulSoup
cao = input("Введите ваш запрос :) : ")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(f"https://www.google.com/search?q={cao}", headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("cite", {"role": "text"})
    item1 = soup_list[0].get_text(strip=True)
    item2 = soup_list[1].get_text(strip=True)
    item3 = soup_list[2].get_text(strip=True)
    clean_url1 = item1.split('›')[0].strip()
    print(f"{clean_url1}")
    clean_url2 = item2.split('›')[0].strip()
    print(f"{clean_url2}")
    clean_url3 = item3.split('›')[0].strip()
    print(f"{clean_url3}")
import sqlite3
connection = sqlite3.connect("itstep_DB.sl3")
cur = connection.cursor()
cur.execute("CREATE TABLE first_table (Sites TEXT),(Amounts NUMBERS);")
def abc(url):
    cur.execute("SELECT * FROM first_table WHERE Sites = ?", (url,))
    existing_site = cur.fetchone()
    if existing_site:
        cur.execute("UPDATE first_table SET Amounts = Amounts+ 1 WHERE sites = ?", (url,))
    else:
        cur.execute("INSERT INTO first_table (Sites, Amounts) VALUES (?, ?)", (url, 1))
abc(clean_url1)
abc(clean_url2)
abc(clean_url3)
connection.commit()
connection.close()
