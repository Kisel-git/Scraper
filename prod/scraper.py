import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import random

auto = []
prox = {"https": "http://87.247.186.40:1080", "http": "http://50.222.245.50:80"}
head = {"Accept": "*/*",
           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}
url = "https://www.avito.ru/moskva/avtomobili/bmw-ASgBAgICAUTgtg3klyg?cd=1&p=2&radius=3000&searchRadius=3000&p="
page = 1
while page < 30:
    get = requests.get(url + str(page), headers=head, proxies=prox)
    soup = BeautifulSoup(get.text, "lxml")
    # Обход ловушки для парсеров (Этот код пропускает любую ссылку с атрибутом code>display: none в атрибуте style, что является общей характеристикой ссылок honeypot.)
    for link in soup.select('a'):
        if 'display' in link.get('style', '') and 'none' in link['style']:
            continue
    auto_info = soup.find_all("div", class_="iva-item-body-KLUuy")
    if auto_info is not []:
        auto.extend(auto_info)
        # сделаем задержку по времени между запросами чтобы уменьшить нагрузку на сайт
        time_delay = random.random()
        scaled_time_delay = 1 + (time_delay * (9 - 5))
        time.sleep(scaled_time_delay)
    else:
        print("Больше данных нет")
        break
    page += 1
print(auto)
count = 0
lst_info = []
lst_price = []
lst_description = []
while count < len(auto):
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
    count += 1
df1 = pd.DataFrame({"Стоимость": lst_price, "Общие сведения": lst_info})
df2 = pd.DataFrame({"Подробное описание": lst_description})
print(df1)
print(df2)








