import requests
import bs4
import csv
from time import sleep
from random import randint



file=open('sandrosfile.csv','w', encoding='UTF-8',newline='\n')
item=1
file_obj=csv.writer(file)
file_obj.writerow(['modeli', 'fasi'])



while item < 6:
    url=f'https://technoshop.ge/index.php?route=product/category&path=56&page={item}'
    pasuxi=requests.get(url)
    noc=pasuxi.text
    soup=bs4.BeautifulSoup(noc, 'html.parser')
    yvelaferi=soup.find('div',{'class':'products-list row grid'})
    erticali=yvelaferi.find_all('div', {'class': 'product-layout'})
    for each in erticali:
        name=each.find('div',{'class': 'caption'})
        bolo_saxeli=name.h4.a.text
        fasi=each.find('span',{'class':'price-new'})
        bolo_fasi=fasi.text
        file_obj.writerow([bolo_saxeli,bolo_fasi])

    item+=1
    sleep(randint(15,20))
