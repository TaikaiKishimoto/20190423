# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib3
import re
import csv
import pprint

with open('your csv file path', 'a', newline='') as f:
    writer = csv.writer(f)
    
    from urllib3.exceptions import InsecureRequestWarning
    urllib3.disable_warnings(InsecureRequestWarning)

    url = input()

    http = urllib3.PoolManager()
    r = http.request('GET', url)

    soup = BeautifulSoup(r.data, 'html.parser')
    title = soup.find('h2').text

    title_strip =  title.split()
    print (title_strip[1] + title_strip[2] )

    class_soup = []
    
    for s in (soup.find_all('td',class_=re.compile(""))):
        class_soup.append(s.text)

    for num,lines in enumerate(class_soup):
        m = re.search(r'(\d{1})/(\d)',str(lines))
        if m != None:
            csvlist = []
            csvlist.append(str(title_strip[1] + title_strip[2]))
            csvlist.extend([str(url),' '])

            print(lines)
            print(class_soup[num+1])
            print(class_soup[num+2])
            if class_soup[num+1] =='1':
                csvlist.extend(['2019/' + lines + ' 9:20','2019/' + lines + ' 10:50'])
            
            if class_soup[num+1] =='2':
                csvlist.extend(['2019/' + lines + ' 11:00','2019/' + lines + ' 12:30'])
            
            if class_soup[num+1] =='3':
                csvlist.extend(['2019/' + lines + ' 13:30','2019/' + lines + ' 15:00'])
            
            if class_soup[num+1] =='4':
                csvlist.extend(['2019/' + lines + ' 15:10','2019/' + lines + ' 16:40'])

            if class_soup[num+1] =='5':
                csvlist.extend(['2019/' + lines + ' 16:50','2019/' + lines + ' 18:20'])

            if class_soup[num+1] =='6':
                csvlist.extend(['2019/' + lines + ' 18:30','2019/' + lines + ' 20:00'])
            
            csvlist.append(str(class_soup[num+2]))
            writer.writerow(csvlist)
        else:
            pass
