from selenium import webdriver
     
options = webdriver.ChromeOptions()     
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

PATH = r"C:\Users\Peter\Documents\GitHub\WebScraping\chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)

url = "https://chp-dashboard.geodata.gov.hk/covid-19/web/main.html?lang=zh"
driver.get(url)

confirmed = driver.find_element_by_id("confirmed").text
discharged = driver.find_element_by_id("discharged").text
hospitalized = driver.find_element_by_id("hospitalized").text
death = driver.find_element_by_id("death").text

driver.quit()

data = [confirmed, hospitalized, discharged, death]
population = 7500000

for i in range(0, 4):
    data[i] = int(data[i].replace(',', ''))

print("Total Case:", data[0])
print("Currently Hospitalisd:", data[1])
print("Discharged:", data[2])
print("Death:", data[3], '\n')

print("Infection rate:", round(float(data[0]/population)*100, 3), "%")
print("Death rate:", round(float(data[3]/data[0])*100, 4), "%\n")

print("Press any key to quit this program...")
input()