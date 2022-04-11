# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 22:32:56 2022

@author: eniya
"""

import pandas as pd
from selenium import *
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome(executable_path="C:\\Users\\eniya\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.covid19india.org/")

timeout=10
try:
    WebDriverWait(driver, timeout).until(EC.visibility_of_all_elements_located((By.CLASS_NAME,"level-vaccinated")))
except TimeoutException:
    driver.quit()
    
category_element=driver.find_element(By.CLASS_NAME,"Table").text
category_list=category_element.split('\n')
print(category_list)

temp=category_list[38]

up_arrow=chr(8593)
down_arrow=chr(8595)

for x in category_list:
    for y in range(len(x)):
        i=x[y]
        if i ==up_arrow:
            category_list.remove(x)
        if i==down_arrow:
            category_list.remove(x)
print(category_list)
print(len(category_list))
total_rows=(len(category_list)-2)/7
print("total rows:", total_rows)
 
data_for_table=[]
i=2
j=9
num_row=0
count=9
while num_row<total_rows:
    temp_list=[]
    while i<j:
        temp_list.append(category_list[i])
        i=i+1
        count=count+1
    data_for_table.append(temp_list)
    j=count
    num_row=num_row+1

print(data_for_table)
column_names=data_for_table[0]
data_for_table.pop(0)

print("new data:", data_for_table)
df=pd.DataFrame(data_for_table,columns=column_names)

print(df)
df.to_csv("covid19_data.csv")

driver.quit()
