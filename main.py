from sa_module import sa
from qa_module import qa
from web_scraping import sikayet_bul
from  bloomberght_scraping import bloomberg_ht

complaints= sikayet_bul("turkcell")

deneme= bloomberg_ht()



for text in deneme:
    if __name__ == "__main__" :
        sen_t = sa(text)[0]["label"]

        print(sen_t)


