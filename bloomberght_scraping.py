import requests
from bs4 import BeautifulSoup as bs


the_base= "https://www.bloomberght.com/borsa"

headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36")
    }

def bloomberg_ht():
    r = requests.get(the_base, headers=headers)
    soup = bs(r.content, "html.parser")

    contents = soup.find_all("div", {"class": "box box-4 item"})

    all_texts = []
    for content in contents:
        ap_link = content.find("a", href=True)["href"]
        new_url = "https://www.bloomberght.com/" + ap_link
        new_r = requests.get(new_url, headers=headers)
        new_soup = bs(new_r.content, "html.parser")
        new_content = new_soup.find("article", {"class": "content"}).get_text(strip=True)
        all_texts.append(new_content)

    return all_texts