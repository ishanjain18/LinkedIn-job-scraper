from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint
from json import dumps


# creates instance of Chrome WebDriver
driver = webdriver.Chrome()

# .get navigates to webpage
driver.get("https://www.mymajors.com/career-list/")

# A list of career types
careerTypes = driver.find_elements(By.CLASS_NAME, "hasChildMenu")

# finds jobs for each career type in careerTypes and store it in a dictionary
careerMap = {}

for career in careerTypes[:-1]:

    career.click()

    # curate list of all jobs within a career into a list variable called jobs
    jobList = driver.find_elements(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/a")
    jobs = [job.text for job in jobList]

    # assigned all jobs to their respective career type
    careerMap[career.text] = jobs
pprint(careerMap)

with open("careers.txt", 'w') as f:
    f.write(dumps(careerMap))

driver.close()