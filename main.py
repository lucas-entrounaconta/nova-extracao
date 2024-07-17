from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
driver = webdriver.Chrome()

url = "https://sistema.novafinanceira.com/index.php?rt=logout"
login = "1968.rayane"
password = "rAYANE@0085590548"
initial_date = "30/06/2024"
final_date = "15/07/2024"

driver.maximize_window()
driver.get(url)

#logging
driver.find_element(By.ID, "usuario").send_keys(login)
driver.find_element(By.ID, "senha").send_keys(password)
print("logando")
#click to login
driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/form/div[3]/input").click()
#nav to menu
driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[4]/a/div/i").click()
driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[5]/a[4]/i").click()
sleep(5)


#searching data
driver.find_element(By.ID, "data_inicio").send_keys(initial_date)
driver.find_element(By.ID,"data_fim").send_keys(final_date)

#download
driver.find_element(By.ID,"ed-download-arquivo-contratos-digitados").click()





