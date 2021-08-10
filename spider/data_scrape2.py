# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 16:11:51 2021

@author: lenovo
"""
import requests
from bs4 import BeautifulSoup
import csv
urls = [
       'https://webbook.nist.gov/cgi/cbook.cgi?ID=C7697372&Units=SI&Mask=1#Thermo-Gas',
       'https://webbook.nist.gov/cgi/cbook.cgi?ID=C111659&Units=SI&Mask=1#Thermo-Gas',
       'https://webbook.nist.gov/cgi/cbook.cgi?ID=C124389&Units=SI&Mask=1#Thermo-Gas',
       'https://webbook.nist.gov/cgi/cbook.cgi?Name=water&Units=SI&Mask=1#Thermo-Gas',
       'https://webbook.nist.gov/cgi/cbook.cgi?Name=hydrogen&Units=SI&Mask=1#Thermo-Gas',
       'https://webbook.nist.gov/cgi/cbook.cgi?Name=CO&Units=SI&Mask=1#Thermo-Gas',
       'https://webbook.nist.gov/cgi/cbook.cgi?Name=O2&Units=SI&Mask=1#Thermo-Gas',
       'https://webbook.nist.gov/cgi/cbook.cgi?Name=N2&Units=SI&Mask=1#Thermo-Gas',
       'https://webbook.nist.gov/cgi/cbook.cgi?ID=C3352576&Units=SI&Mask=1#Thermo-Gas',
       'https://webbook.nist.gov/cgi/cbook.cgi?ID=C10102439&Units=SI&Mask=1#Thermo-Gas',
       'https://webbook.nist.gov/cgi/cbook.cgi?ID=C17778802&Units=SI&Mask=1#Thermo-Gas',
       'https://webbook.nist.gov/cgi/cbook.cgi?ID=C7440440&Units=SI&Mask=2#Thermo-Condensed',
       'https://webbook.nist.gov/cgi/cbook.cgi?ID=C12385136&Units=SI&Mask=1#Thermo-Gas',
       ]

csv_file = open('cbs_srape2.csv', 'w', newline='')
for url in urls:
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    # 写入csv文件
    csv_writer = csv.writer(csv_file)
    
    # 提取源码数据  

    fit_table = soup.find('table', {'aria-label': "Gas Phase Heat Capacity (Shomate Equation)"  })
    fit_name = soup.find('main').h1.text
    print(fit_name)
    
    # print(fit_val.prettify())
    f_values = []
    fit_field = [fit_name]
    try:
        fit_tr = fit_table.find_all('tr')
    except Exception as e :
        csv_writer.writerow(fit_field)
    else:
        for k, iter in enumerate(fit_tr):

            fit_field.append(iter.th.text)

            fit_td = iter.find_all('td')

            # 创建二重列表
            if k == 0:
                for m in range(len(fit_td)):
                    f_values.append([''])

            for i, f_value in enumerate(fit_td):
                f_values[i].append(f_value.text)

        print(fit_field)
        print(f_values)

        csv_writer.writerow(fit_field)
        for i in range(len(fit_td)):
            csv_writer.writerow(f_values[i])
    print()


csv_file.close()
