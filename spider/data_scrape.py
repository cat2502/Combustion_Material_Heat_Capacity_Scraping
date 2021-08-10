# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 20:11:08 2021

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

csv_file = open('cbs_srape.csv2','w',newline = '')
for str in urls:
    source = requests.get(str).text
    soup = BeautifulSoup(source,'lxml')

    # 写入csv文件
    csv_writer = csv.writer(csv_file)
    
    # 提取源码数据  

    fit_table = soup.find('table', {'aria-label':"Gas Phase Heat Capacity (Shomate Equation)"  })
    fit_name = soup.find('main').h1.text
    print(fit_name)
    
    #print(fit_val.prettify())
    try:
        fit_tr = fit_table.find_all('tr') 
        fit_field = [fit_name]
        fit_value = ['']
        for iter in fit_tr:
            fit_field.append(iter.th.text)
            fit_value.append(iter.td.text)
            
        print(fit_field)
        print(fit_value)
        csv_writer.writerow(fit_field)
        csv_writer.writerow(fit_value)
    except Exception as e :
        pass


csv_file.close()

