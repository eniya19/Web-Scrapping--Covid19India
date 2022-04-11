# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 20:48:20 2022

@author: eniya
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 19:39:57 2022

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
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME,"level-vaccinated")))
except TimeoutException:
    driver.quit()

cases_current_stats=driver.find_element(By.CLASS_NAME,"Level").text;
print(cases_current_stats)

cs_list=cases_current_stats.split('\n')
print(cs_list)

print('Today Confirmed:', cs_list[1])
print('Confirmed:', cs_list[2])
print("Active:",cs_list[4])
print('Todays Recovered:',cs_list[6])
print("Recovered:",cs_list[7])
print("Today Deceased:",cs_list[9])
print("Deceased:", cs_list[10])

tested_current_stats= driver.find_element(By.CLASS_NAME,"header-right")
print("Total Tested:",tested_current_stats.text.split('\n')[1])

vaccination_current_stats=driver.find_element(By.CLASS_NAME,"level-vaccinated")
vcs=vaccination_current_stats.text.split('\n')[0]

vaccination_alo_prog_bar=driver.find_element(By.CLASS_NAME,"progress-bar")
vaccination_fv_prog_bar=driver.find_element_by_class_name("label")

fvl=vaccination_fv_prog_bar[1].text
fvl=fvl.split('(')
fvl=fvl[1].split(')')


print("Total Vaccine Doses:",vcs)
print("Atleast one dose:",vaccination_alo_prog_bar.text)
print("fully vaccinated:", fvl[0])





