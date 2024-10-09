import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import random

# Получение данных с первой страницы сайта и сохранения их в файл
#auto = []
#prox = {"https": "http://178.218.44.79:3128", "http": "http://72.10.164.178:33135"}
#head = {"Accept": "*/*",
 #          "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}
#url = "https://www.avito.ru/moskva/avtomobili/bmw-ASgBAgICAUTgtg3klyg?cd=1&p=2&radius=3000&searchRadius=3000&p=1"
#get = requests.get(url, headers=head, proxies=prox)
#res = get.text
#with open("/Users/user/Desktop/book3.html", "w") as file_in:
  #file_in.write(res)
auto = []
lst_info = []
lst_price = []
lst_description = []
with open("page.html", "r") as file_read:
    stran = file_read.read()
soup = BeautifulSoup(stran, "lxml")
auto_info = soup.find_all("div", class_="iva-item-body-KLUuy")
auto.extend(auto_info)
for elem in auto:
    price = elem.find("strong", class_="styles-module-root-bLKnd")
    if price is not None:
        price = price.text
    else:
        price = "No info"
    info = elem.find("h3", itemprop="name")
    if info is not None:
        info = info.text
    else:
        info = "No info"
    description = elem.find("p", class_="styles-module-root-YczkZ styles-module-size_s-xb_uK styles-module-size_s_compensated-QmHFs styles-module-size_s-_z7mI styles-module-ellipsis-a2Uq1 stylesMarningNormal-module-root-S7NIr stylesMarningNormal-module-paragraph-s-Yhr2e styles-module-noAccent-LowZ8 styles-module-root_bottom-G4JNz styles-module-margin-bottom_6-_aVZm")
    if description is not None:
        description = description.text
    else:
        description = "No info"
    lst_price.append(price)
    lst_info.append(info)
    lst_description.append(description)
df1 = pd.DataFrame({"Стоимость": lst_price, "Общие сведения": lst_info})
df2 = pd.DataFrame({"Подробное описание": lst_description})
print(df1)
print(df2)