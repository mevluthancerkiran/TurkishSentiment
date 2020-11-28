import requests
from bs4 import BeautifulSoup as bs


def sikayet_bul(key_word):
    site = "https://www.sikayetvar.com/"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36")
    }

    baslik = key_word
    r = requests.get(site + baslik, headers=headers)

    if r.status_code != 200:
        print("Nothing is found.")
    else:
        soup = bs(r.content, "html.parser")
        entries = soup.find("div", {"class": "brandsearch-cards clearfix"}).find_all("article")

    all_contents = []

    for num, entry in enumerate(entries, 1):
        content_url = entry.find("p", "card-text").find("a", href=True)["href"]
        content_url= "https://www.sikayetvar.com"+ content_url
        #print(content_url)
        new_r= requests.get(content_url, headers=headers)
        new_soup= bs(new_r.content, "html.parser")
        content= new_soup.find("div", {"class": "card-text"}).get_text(strip=True)
        all_contents.append(content)

    return all_contents