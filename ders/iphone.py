from bs4 import BeautifulSoup
import requests

while True:
 url = "https://www.vatanbilgisayar.com/iphone-11-64-gb-akilli-telefon-beyaz.html"
 sayfa = requests.get(url)

 html_sayfa = BeautifulSoup(sayfa.content,"html.parser")

 isim = html_sayfa.find("h1" ,class_="product-list__product-name").getText()

 print(isim)

 fiyat = html_sayfa.find("span",class_="product-list__price").getText()

 print(fiyat)


 #Telegram
 import time

 api = "https://api.telegram.org/bot5639382705:AAErUjCZfUA0Etg_75SKfDRYSn14OuoHjUc/SendMessage"

 mesaj = isim + "\n" + fiyat

 requests.post(url=api,data={"chat_id":"6057055919","text":mesaj}).json()

 time.sleep(60)






